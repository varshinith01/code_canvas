from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('constitution.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- PAGE ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/library')
def library():
    conn = get_db_connection()
    articles = conn.execute('SELECT * FROM articles').fetchall()
    conn.close()
    return render_template('library.html', articles=articles)

# --- SMART SEARCH LOGIC ---
def smart_search(user_query):
    # 1. Define Context Words (Low Priority)
    context_map = {
        'student': ['student', 'college', 'exam', 'university', 'ragging', 'admission', 'school', 'teacher', 'class'],
        'nri': ['nri', 'abroad', 'visa', 'passport', 'oci', 'non-resident', 'foreigner'],
        'gov_employee': ['govt', 'government', 'bureaucrat', 'ias', 'ips', 'civil service', 'suspension', 'official'],
        'pvt_employee': ['private', 'corporate', 'manager', 'boss', 'firing', 'layoff', 'salary', 'company', 'mnc'],
        'politician': ['politician', 'mp', 'mla', 'election', 'campaign', 'vote', 'candidate', 'politics', 'party', 'leader'],
        'ngo': ['ngo', 'activist', 'social worker', 'protest', 'rights', 'welfare', 'foundation', 'charity']
    }

    # 2. Detect Context & Build Low Priority Set
    detected_context = None
    all_context_words = set()
    user_query_lower = user_query.lower()
    
    for role, keywords in context_map.items():
        for kw in keywords:
            all_context_words.add(kw)
            if kw in user_query_lower and detected_context is None:
                detected_context = role

    # 3. Clean Query
    noise_words = {
        'how', 'do', 'i', 'can', 'should', 'why', 'what', 'is', 'are', 'am', 'was', 'were',
        'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'by', 'with', 'from',
        'my', 'me', 'you', 'your', 'he', 'she', 'it', 'they', 'we', 'us',
        'be', 'been', 'being', 'have', 'has', 'had', 'will', 'would', 'could',
        'about', 'tell', 'say', 'give', 'show', 'find', 'search', 'look', 'allowed', 'get'
    }

    raw_words = user_query_lower.replace('?', '').replace('.', '').replace(',', '').split()
    search_words = [w for w in raw_words if w not in noise_words and (len(w) > 2 or w in ['14','15','19','21'])]

    # 4. Score Articles
    conn = get_db_connection()
    articles = conn.execute('SELECT * FROM articles').fetchall()
    conn.close()

    best_match = None
    highest_score = 0
    matched_reasons = []

    for article in articles:
        score = 0
        reasons = []
        
        art_num = article['article_number'].lower().replace('article', '').strip()
        db_keywords = article['keywords'].lower().split()
        
        for word in search_words:
            # A. Exact Article Number (Instant Win)
            if word == art_num:
                score += 100
                reasons.append(f"Article {word}")
            
            # B. Keyword Match
            elif word in db_keywords:
                # If it's a context word (like "government"), give it LOW points
                if word in all_context_words and word not in ['vote', 'ragging', 'salary', 'arrest', 'speech']:
                    score += 1
                    # reasons.append(f"Context '{word}'") # Don't clutter UI with this
                else:
                    # High value match
                    score += 10
                    reasons.append(f"Keyword '{word}'")
        
        if score > highest_score:
            highest_score = score
            best_match = article
            matched_reasons = reasons

    if highest_score < 5: 
        return None, "LOW_CONFIDENCE", [], detected_context
        
    return best_match, "SUCCESS", matched_reasons, detected_context

# --- API ROUTE ---
@app.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.json
    user_query = data.get('question', '')
    
    article, status, reasons, detected_ctx = smart_search(user_query)
    
    if status != "SUCCESS":
        return jsonify({
            "error": "I couldn't find a specific legal answer for that. Please try asking about 'Equality', 'Arrest', 'Jobs', 'Voting' or 'Education'."
        })
        
    context_note = None
    if detected_ctx:
        role_map = {
            'student': 'student_view', 'nri': 'nri_view', 'gov_employee': 'gov_emp_view',
            'pvt_employee': 'pvt_emp_view', 'politician': 'politician_view', 'ngo': 'ngo_view'
        }
        col = role_map.get(detected_ctx)
        if col and article[col] and article[col] != "N/A":
            context_note = article[col]
            reasons.append(f"Context: {detected_ctx.capitalize()}")

    return jsonify({
        "answer": article['explanation'],
        "source": article['article_number'],
        "legal_text": article['text'],
        "source_link": article['link'],
        "context_note": context_note,
        "logic_trace": f"Matched: {', '.join(reasons)}."
    })

if __name__ == '__main__':
    app.run(debug=True)