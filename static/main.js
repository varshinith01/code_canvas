document.addEventListener('DOMContentLoaded', () => {
  // Chat handling
  const chatForm = document.getElementById('chatForm');
  const chatWindow = document.getElementById('chatWindow');
  const chatInput = document.getElementById('chatInput');

  function scrollChatToBottom() {
    if (chatWindow) chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  function createUserBubble(text) {
    const wrap = document.createElement('div');
    wrap.className = 'flex justify-end';
    const bubble = document.createElement('div');
    bubble.className = 'max-w-[85%] bg-emerald-700 text-white p-4 rounded-2xl rounded-tr-none shadow-sm';
    bubble.textContent = text;
    wrap.appendChild(bubble);
    return wrap;
  }

  function createLoadingBubble() {
    const wrap = document.createElement('div');
    wrap.className = 'flex justify-start';
    const bubble = document.createElement('div');
    bubble.className = 'bg-white border border-stone-200 rounded-2xl rounded-tl-none px-6 py-4 text-stone-500 italic shadow-sm';
    bubble.textContent = 'Consulting the Constitution...';
    wrap.appendChild(bubble);
    return {wrap, bubble};
  }

  function createAICard(answer, logic, source, legal_text, context_note) {
    const wrapper = document.createElement('div');
    wrapper.className = 'flex justify-start w-full';

    const card = document.createElement('div');
    card.className = 'bg-white border border-stone-200 rounded-2xl rounded-tl-none shadow-sm overflow-hidden max-w-[90%] md:max-w-2xl';

    // 1. Main Answer
    const p = document.createElement('div');
    p.className = 'p-6 text-stone-800 text-lg leading-relaxed';
    p.textContent = answer; // Secure text content
    card.appendChild(p);

    // 2. Context Note (If available)
    if (context_note) {
        const ctxDiv = document.createElement('div');
        ctxDiv.className = 'bg-amber-50 border-l-4 border-amber-400 p-4 m-6 mt-0 text-stone-700 text-sm';
        // Note: We use innerHTML here because your DB has bold tags (**). 
        // For safety in production, use a markdown parser, but for this project, simple replace is fine.
        ctxDiv.innerHTML = context_note.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        card.appendChild(ctxDiv);
    }

    // 3. Logic Trace
    const metaDiv = document.createElement('div');
    metaDiv.className = 'bg-stone-50 px-6 py-3 border-t border-stone-100 flex items-start gap-2';
    metaDiv.innerHTML = `<span class="text-amber-500 mt-1">💡</span><p class="text-xs text-stone-500 font-mono">${logic}</p>`;
    card.appendChild(metaDiv);

    // 4. Source & Legal Text
    if (source && legal_text) {
      const sourceDiv = document.createElement('div');
      sourceDiv.className = 'border-t border-stone-200 p-6 bg-stone-50/50';
      sourceDiv.innerHTML = `
        <p class="text-xs font-bold text-emerald-700 uppercase tracking-wider mb-2">Source: ${source}</p>
        <p class="font-serif text-stone-600 italic text-sm">"${legal_text}"</p>
      `;
      card.appendChild(sourceDiv);
    }

    wrapper.appendChild(card);
    return wrapper;
  }

  if (chatForm) {
    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const q = chatInput.value.trim();
      if (!q) return;

      // Append user bubble
      chatWindow.appendChild(createUserBubble(q));
      chatInput.value = '';
      scrollChatToBottom();

      // Show loading
      const {wrap: loadingWrap} = createLoadingBubble();
      chatWindow.appendChild(loadingWrap);
      scrollChatToBottom();

      try {
        const res = await fetch('/api/chat', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({question: q})
        });
        const data = await res.json();

        // remove loading
        loadingWrap.remove();

        if (data.error) {
           // Display error as a simple card
           const errWrap = document.createElement('div');
           errWrap.className = 'flex justify-start';
           errWrap.innerHTML = `<div class="bg-red-50 text-red-600 p-4 rounded-2xl rounded-tl-none border border-red-100">${data.error}</div>`;
           chatWindow.appendChild(errWrap);
        } else {
          const aiCard = createAICard(
              data.answer, 
              data.logic_trace, 
              data.source, 
              data.legal_text, 
              data.context_note // Pass the context note
          );
          chatWindow.appendChild(aiCard);
        }

        scrollChatToBottom();
      } catch (err) {
        loadingWrap.remove();
        console.error(err);
      }
    });
  }
});