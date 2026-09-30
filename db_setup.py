import sqlite3

def init_db():
    conn = sqlite3.connect('constitution.db')
    cursor = conn.cursor()
    
    cursor.execute('DROP TABLE IF EXISTS articles')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            article_number TEXT NOT NULL,
            part TEXT NOT NULL,
            text TEXT NOT NULL,
            explanation TEXT NOT NULL,
            keywords TEXT NOT NULL,
            link TEXT NOT NULL,
            student_view TEXT DEFAULT "N/A",
            nri_view TEXT DEFAULT "N/A",
            gov_emp_view TEXT DEFAULT "N/A",
            pvt_emp_view TEXT DEFAULT "N/A",
            politician_view TEXT DEFAULT "N/A",
            ngo_view TEXT DEFAULT "N/A"
        )
    ''')
    
    # --- OFFICIAL LINKS ---
    LINK_FULL = "https://legislative.gov.in/sites/default/files/COI...pdf"
    LINK_PART_3 = "https://www.mea.gov.in/images/pdf1/part3.pdf"   # Fundamental Rights
    LINK_PART_4 = "https://www.mea.gov.in/images/pdf1/part4.pdf"   # Directive Principles
    LINK_PART_4A = "https://www.mea.gov.in/images/pdf1/part4A.pdf" # Fundamental Duties
    LINK_PART_15 = "https://www.mea.gov.in/Images/pdf1/Part15.pdf" # Elections
    
    articles = [
        {
            "article_number": "Preamble",
            "part": "Introduction",
            "text": "We, the people of India... give to ourselves this Constitution.",
            "explanation": "The Preamble is the identity card of the Indian Constitution. It declares India to be a Sovereign, Socialist, Secular, Democratic Republic. It promises Justice, Liberty, Equality, and Fraternity to all citizens. It establishes that the ultimate power lies with the people ('We, the People'). It guides the interpretation of all other laws in the country.",
            "keywords": "preamble introduction start secular democratic republic justice india sovereign socialist fraternity liberty",
            "link": LINK_FULL,
            "student_view": "🎓 **Student:** Learn these values. They are the foundation of your civics education.",
            "nri_view": "🌍 **NRI:** It defines the nation you belong to. 'Sovereign' means no foreign power rules us.",
            "gov_emp_view": "🏛️ **Gov Employee:** You serve the 'Republic' defined here, not any individual master.",
            "pvt_emp_view": "💼 **Private Employee:** The promise of 'Social Justice' ensures labor laws protect you.",
            "politician_view": "🗳️ **Politician:** You swear allegiance to these ideals. Deviating from Secularism or Democracy violates your oath.",
            "ngo_view": "🤝 **NGO:** Your work usually fights for the Justice and Equality promised here."
        },
        {
            "article_number": "Article 14",
            "part": "Part III - Fundamental Rights",
            "text": "The State shall not deny to any person equality before the law...",
            "explanation": "Article 14 guarantees 'Equality before the Law' and 'Equal Protection of the Laws'. It means that no person is above the law, whether rich, poor, or powerful. The government cannot discriminate against any individual without a valid, logical reason. It ensures fairness in state actions, meaning arbitrary dismissals, biased rules, or unfair treatment by public officials can be challenged in court. This is the foundation of the Rule of Law in India.",
            "keywords": "14 equality law fairness justice equal bias rule discrimination suspend suspension arbitrary treat same",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Grading and admissions must be fair. No special treatment for VIP kids.",
            "nri_view": "🌍 **NRI:** You are entitled to equal legal protection in India, just like any citizen.",
            "gov_emp_view": "🏛️ **Gov Employee:** You cannot be suspended or treated arbitrarily by superiors without a valid reason.",
            "pvt_emp_view": "💼 **Private Employee:** Protects you from arbitrary government interference in your work or licensing.",
            "politician_view": "🗳️ **Politician:** You are subject to the same laws as the common man. No VIP immunity in criminal cases.",
            "ngo_view": "🤝 **NGO:** Use this to fight for beneficiaries who are being discriminated against by state officials."
        },
        {
            "article_number": "Article 15",
            "part": "Part III - Fundamental Rights",
            "text": "Prohibition of discrimination on grounds of religion, race, caste, sex or place of birth.",
            "explanation": "Article 15 strictly prohibits the State from discriminating against any citizen on grounds of religion, race, caste, sex, or place of birth. It ensures equal access to public spaces like shops, hotels, wells, tanks, and roads. While it mandates equality, it also allows the State to make 'special provisions' for women, children, and socially backward classes (like SC/STs). This is the basis for affirmative action and reservation policies in India.",
            "keywords": "15 discrimination caste religion gender race public places access shop hotel reservation women sc st",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** You cannot be denied entry to a library or playground based on your caste or religion.",
            "nri_view": "🌍 **NRI:** Applies only to CITIZENS. Foreign citizens may not claim full protection here.",
            "gov_emp_view": "🏛️ **Gov Employee:** You cannot discriminate against citizens in the discharge of your duties.",
            "pvt_emp_view": "💼 **Private Employee:** Workplace harassment based on gender (POSH) draws spirit from this.",
            "politician_view": "🗳️ **Politician:** You cannot favor your own community in distributing public resources.",
            "ngo_view": "🤝 **NGO:** Primary tool to fight social exclusion and caste-based denial of services."
        },
        {
            "article_number": "Article 16",
            "part": "Part III - Fundamental Rights",
            "text": "Equality of opportunity in matters of public employment.",
            "explanation": "Article 16 ensures equal opportunity for all citizens in matters of government employment. No citizen can be ineligible for a state job based on religion, caste, sex, descent, or place of birth. However, it allows the State to reserve posts for backward classes who are not adequately represented in services. It balances merit with social justice, ensuring that public offices are open to all.",
            "keywords": "16 jobs employment work government hiring reservation promotion vacancy public service",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Ensures fair competition for UPSC/SSC exams. No bias in selection.",
            "nri_view": "🌍 **NRI:** Gov jobs are reserved for Indian Citizens. You may need to regain citizenship to apply.",
            "gov_emp_view": "🏛️ **Gov Employee:** Protects you against discrimination in promotions and transfers.",
            "pvt_emp_view": "💼 **Private Employee:** N/A (Applies to State jobs, but sets a benchmark for fairness).",
            "politician_view": "🗳️ **Politician:** You cannot influence hiring processes for voters/supporters illegally.",
            "ngo_view": "🤝 **NGO:** Use this to fight for marginalized groups denied government jobs."
        },
        {
            "article_number": "Article 17",
            "part": "Part III - Fundamental Rights",
            "text": "Abolition of Untouchability.",
            "explanation": "Article 17 abolishes 'Untouchability' in any form. The practice of untouchability is a punishable offense under the law. It forbids enforcing disabilities on anyone arising out of 'untouchability', such as refusing service in a shop or entry to a temple. This is one of the few absolute rights available against private individuals as well. It aims to eradicate the historic social evil of caste-based exclusion.",
            "keywords": "17 untouchability caste dalit sc st discrimination social justice ragging bully harassment",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Ragging or bullying based on caste is a serious crime under this article.",
            "nri_view": "🌍 **NRI:** Practicing caste discrimination abroad can still attract legal trouble in India.",
            "gov_emp_view": "🏛️ **Gov Employee:** Strict action is taken against officials practicing untouchability.",
            "pvt_emp_view": "💼 **Private Employee:** Zero tolerance for caste slurs in the corporate workplace.",
            "politician_view": "🗳️ **Politician:** Promoting caste hatred disqualifies you from elections.",
            "ngo_view": "🤝 **NGO:** The SC/ST Prevention of Atrocities Act is based on this Article."
        },
        {
            "article_number": "Article 19",
            "part": "Part III - Fundamental Rights",
            "text": "Protection of certain rights regarding freedom of speech, etc.",
            "explanation": "Article 19 is known as the 'backbone' of fundamental rights. It guarantees six essential freedoms: (a) Freedom of speech and expression, (b) To assemble peaceably without arms, (c) To form associations or unions, (d) To move freely throughout India, (e) To reside in any part of India, and (g) To practice any profession, trade, or business. However, these rights are not absolute and can be restricted for national security or public order.",
            "keywords": "19 speech protest media travel move business trade union internet blog criticize social media tweet post express",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Right to protest peacefully and form student unions.",
            "nri_view": "🌍 **NRI:** These freedoms are exclusively for CITIZENS. Foreigners do not have Art 19 rights.",
            "gov_emp_view": "🏛️ **Gov Employee:** Your speech is restricted by service conduct rules (no criticizing govt).",
            "pvt_emp_view": "💼 **Private Employee:** You can form unions. However, trade secrets are not 'free speech'.",
            "politician_view": "🗳️ **Politician:** Allows you to campaign and criticize the opposition (without hate speech).",
            "ngo_view": "🤝 **NGO:** Essential for advocacy, holding rallies, and publishing reports."
        },
        {
            "article_number": "Article 20",
            "part": "Part III - Fundamental Rights",
            "text": "Protection in respect of conviction for offenses.",
            "explanation": "Article 20 provides protection to persons accused of crimes. It guarantees three rights: (1) No Ex-post-facto law (you can't be punished for an act that wasn't a crime when you did it), (2) No Double Jeopardy (you can't be prosecuted twice for the exact same offense), and (3) No Self-Incrimination (you cannot be forced to be a witness against yourself).",
            "keywords": "20 conviction double jeopardy witness self incrimination punish crime evidence accused",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** You cannot be punished twice by the university for the same mistake.",
            "nri_view": "🌍 **NRI:** You cannot be forced to witness against yourself in Indian courts.",
            "gov_emp_view": "🏛️ **Gov Employee:** Departmental inquiry and Criminal trial can sometimes happen simultaneously.",
            "pvt_emp_view": "💼 **Private Employee:** Protects you if your company tries to frame you legally.",
            "politician_view": "🗳️ **Politician:** Protects you from being targeted by multiple FIRs for the exact same act.",
            "ngo_view": "🤝 **NGO:** Useful when defending activists arrested on false charges."
        },
        {
            "article_number": "Article 21",
            "part": "Part III - Fundamental Rights",
            "text": "No person shall be deprived of his life or personal liberty except according to procedure established by law.",
            "explanation": "Article 21 is the most important right: Protection of Life and Personal Liberty. The Supreme Court has expanded this to include the Right to Privacy, Right to Health, Right to Clean Environment, Right to Livelihood, and Right to Dignity. It means the State cannot take away your freedom or life without following a fair and just legal procedure.",
            "keywords": "21 life liberty privacy health arrest environment pollution dignity boss fire firing layoff job terminate harassment pension ragging bullying safety water food",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Protection from ragging and right to privacy in hostels.",
            "nri_view": "🌍 **NRI:** AVAILABLE TO ALL. Even non-citizens are protected by Art 21 in India.",
            "gov_emp_view": "🏛️ **Gov Employee:** Protection against arbitrary dismissal without a fair hearing.",
            "pvt_emp_view": "💼 **Private Employee:** Protects against sexual harassment and unsafe work environments.",
            "politician_view": "🗳️ **Politician:** You cannot be arrested without due process, even by rivals.",
            "ngo_view": "🤝 **NGO:** The 'Umbrella Right'. Use it to fight for clean water, health, and prisoner rights."
        },
        {
            "article_number": "Article 21A",
            "part": "Part III - Fundamental Rights",
            "text": "The State shall provide free and compulsory education to all children of the age of six to fourteen years.",
            "explanation": "Article 21A guarantees the Right to Education. It mandates that the State must provide free and compulsory education to all children between the ages of 6 and 14 years. This amendment makes education a fundamental right, ensuring that poverty is not a barrier to learning. It puts the responsibility on the government to ensure schools are accessible.",
            "keywords": "21a education school children kid study learn rte free school admission fees",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Guarantees free schooling. Report if a child is denied this.",
            "nri_view": "🌍 **NRI:** Your children in India have rights, though 'free' quota rules vary.",
            "gov_emp_view": "🏛️ **Gov Employee:** Duty to ensure implementation in your district.",
            "pvt_emp_view": "💼 **Private Employee:** Private schools must reserve 25% seats for EWS.",
            "politician_view": "🗳️ **Politician:** Ensure schools in your constituency are functional.",
            "ngo_view": "🤝 **NGO:** Use this to demand admission for slum children."
        },
        {
            "article_number": "Article 22",
            "part": "Part III - Fundamental Rights",
            "text": "Protection against arrest and detention in certain cases.",
            "explanation": "Article 22 safeguards the rights of persons who are arrested. It mandates that (1) The arrested person must be informed of the grounds of arrest, (2) They have the right to consult a lawyer of their choice, and (3) They must be produced before a Magistrate within 24 hours of arrest. It also lays down rules for Preventive Detention.",
            "keywords": "22 arrest detention police jail lawyer magistrate 24 hours warrant custody bail",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** If arrested in a protest, you must be allowed to call a lawyer/family.",
            "nri_view": "🌍 **NRI:** You have the right to contact your embassy/consulate if arrested.",
            "gov_emp_view": "🏛️ **Gov Employee:** Public servants often need sanction before arrest in official duty cases.",
            "pvt_emp_view": "💼 **Private Employee:** Police cannot detain you indefinitely for corporate disputes.",
            "politician_view": "🗳️ **Politician:** Preventive detention is often used against politicians; know your safeguards.",
            "ngo_view": "🤝 **NGO:** The primary tool against illegal police detention of activists."
        },
        {
            "article_number": "Article 23",
            "part": "Part III - Fundamental Rights",
            "text": "Prohibition of traffic in human beings and forced labor.",
            "explanation": "Article 23 prohibits traffic in human beings (selling/buying people), 'begar' (forced work without pay), and other forms of forced labor. This article is a powerful tool against slavery, bonded labor, and human trafficking. It protects individuals from exploitation by landlords, money lenders, or the state.",
            "keywords": "23 forced labor slavery trafficking human exploitation unpaid work begar bond",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** You cannot be forced to do unpaid manual labor by seniors/teachers.",
            "nri_view": "🌍 **NRI:** Strict laws against maid exploitation/withholding passports.",
            "gov_emp_view": "🏛️ **Gov Employee:** You must act if you see bonded labor in your jurisdiction.",
            "pvt_emp_view": "💼 **Private Employee:** Companies cannot force you to work without pay (slavery).",
            "politician_view": "🗳️ **Politician:** Champion the cause of ending bonded labor in your area.",
            "ngo_view": "🤝 **NGO:** Rescue operations for trafficked women/children rely on this."
        },
        {
            "article_number": "Article 24",
            "part": "Part III - Fundamental Rights",
            "text": "No child below the age of fourteen years shall be employed to work in any factory...",
            "explanation": "Article 24 imposes a strict ban on employing children below the age of 14 in factories, mines, or any hazardous employment. It aims to protect the health and safety of children. Note that it specifically bans 'hazardous' work, but other laws (like the Child Labour Act) have expanded this ban to almost all forms of work for children.",
            "keywords": "24 child labor kids factory danger work hazardous mine safety",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Children belong in schools, not factories. Report violations.",
            "nri_view": "🌍 **NRI:** Do not employ minors as domestic help during India visits.",
            "gov_emp_view": "🏛️ **Gov Employee:** Inspect factories for child labor violations.",
            "pvt_emp_view": "💼 **Private Employee:** Ensure your supply chain (vendors) is child-labor free.",
            "politician_view": "🗳️ **Politician:** Advocate for rehabilitation centers for rescued kids.",
            "ngo_view": "🤝 **NGO:** Rescue operations for child laborers rely on this."
        },
        {
            "article_number": "Article 25",
            "part": "Part III - Fundamental Rights",
            "text": "Freedom of conscience and free profession, practice and propagation of religion.",
            "explanation": "Article 25 guarantees all persons the freedom of conscience and the right to freely profess, practice, and propagate religion. This means you can follow any faith (or no faith), worship as you please, and share your beliefs. However, this right is subject to public order, morality, and health. The State can also regulate economic or political activities associated with religious practice.",
            "keywords": "25 religion god faith worship prayer temple church mosque convert votes name election campaign",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** You can follow your faith, but schools can enforce uniforms.",
            "nri_view": "🌍 **NRI:** You are free to visit Indian religious places and worship.",
            "gov_emp_view": "🏛️ **Gov Employee:** You must be secular in duty, regardless of personal faith.",
            "pvt_emp_view": "💼 **Private Employee:** Corporate offices usually respect religious holidays.",
            "politician_view": "🗳️ **Politician:** You can practice faith, but seeking votes in the name of religion is illegal.",
            "ngo_view": "🤝 **NGO:** Defend the rights of minorities to practice their faith."
        },
        {
            "article_number": "Article 29",
            "part": "Part III - Fundamental Rights",
            "text": "Protection of interests of minorities.",
            "explanation": "Article 29 protects the interests of minorities. It states that any section of citizens with a distinct language, script, or culture has the right to conserve it. Furthermore, it ensures that no citizen can be denied admission into any state-maintained or state-aided educational institution on grounds of religion, race, caste, or language.",
            "keywords": "29 minority language culture script admission discrimination heritage",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** You cannot be denied admission to state schools based on language/religion.",
            "nri_view": "🌍 **NRI:** Helps preserve Indian culture/languages.",
            "gov_emp_view": "🏛️ **Gov Employee:** Ensure minority languages are respected in public dealings.",
            "pvt_emp_view": "💼 **Private Employee:** N/A",
            "politician_view": "🗳️ **Politician:** Protect the cultural heritage of your constituents.",
            "ngo_view": "🤝 **NGO:** Work to preserve tribal languages and cultures."
        },
        {
            "article_number": "Article 30",
            "part": "Part III - Fundamental Rights",
            "text": "Right of minorities to establish and administer educational institutions.",
            "explanation": "Article 30 grants all religious and linguistic minorities the right to establish and administer educational institutions of their choice. The State cannot discriminate against any institution in granting aid just because it is managed by a minority. This is why institutions like St. Stephen's or Jamia Millia Islamia have special autonomy.",
            "keywords": "30 minority institution college school establish admin run madrasa convent autonomy",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** Explains why some colleges (St Stephens, Jamia) have specific quotas.",
            "nri_view": "🌍 **NRI:** You can donate/support minority institutions in India.",
            "gov_emp_view": "🏛️ **Gov Employee:** State aid cannot be denied just because an institute is minority-run.",
            "pvt_emp_view": "💼 **Private Employee:** Teachers in these institutions have specific rights.",
            "politician_view": "🗳️ **Politician:** Support minority education infrastructure.",
            "ngo_view": "🤝 **NGO:** Help minority groups set up educational trusts."
        },
        {
            "article_number": "Article 32",
            "part": "Part III - Fundamental Rights",
            "text": "Remedies for enforcement of rights conferred by this Part.",
            "explanation": "Article 32 is called the 'Heart and Soul' of the Constitution. It gives every citizen the right to move the Supreme Court directly if their Fundamental Rights are violated. The Court can issue writs (orders) like Habeas Corpus, Mandamus, etc., to enforce rights. Without Article 32, other rights would be meaningless as there would be no way to enforce them.",
            "keywords": "32 court supreme justice remedy heart soul writ ambedkar lawyer judge pil sue",
            "link": LINK_PART_3,
            "student_view": "🎓 **Student:** If a university illegally cancels admission, go to court.",
            "nri_view": "🌍 **NRI:** You can file writs if your fundamental rights in India are violated.",
            "gov_emp_view": "🏛️ **Gov Employee:** Citizens can use this against YOU if you violate their rights.",
            "pvt_emp_view": "💼 **Private Employee:** Use Habeas Corpus if a colleague is illegally detained.",
            "politician_view": "🗳️ **Politician:** Use this to challenge unconstitutional government orders.",
            "ngo_view": "🤝 **NGO:** Public Interest Litigation (PIL) is filed under this (or Art 226)."
        },
        {
            "article_number": "Article 39A",
            "part": "Part IV - Directive Principles",
            "text": "Equal justice and free legal aid.",
            "explanation": "Article 39A directs the State to ensure that the legal system promotes justice on a basis of equal opportunity.Crucially, it mandates providing free legal aid to the poor and weaker sections. This ensures that opportunities for securing justice are not denied to any citizen by reason of economic or other disabilities. It is the basis for the Legal Services Authorities Act.",
            "keywords": "39a legal aid lawyer free help poor justice court money fee afford expensive defense",
            "link": LINK_PART_4,
            "student_view": "🎓 **Student:** If you have no money for a lawyer, the State must give one.",
            "nri_view": "🌍 **NRI:** Legal aid rules vary for non-citizens.",
            "gov_emp_view": "🏛️ **Gov Employee:** You are entitled to defense if sued for official acts.",
            "pvt_emp_view": "💼 **Private Employee:** Useful if fighting a corporate giant without funds.",
            "politician_view": "🗳️ **Politician:** Promote legal aid clinics in your constituency.",
            "ngo_view": "🤝 **NGO:** Crucial for filing PILs on behalf of the poor."
        },
        {
            "article_number": "Article 41",
            "part": "Part IV - Directive Principles",
            "text": "Right to work, to education and to public assistance in certain cases.",
            "explanation": "Article 41 directs the State to secure the right to work, education, and public assistance in cases of unemployment, old age, sickness, and disablement. It is the constitutional basis for social welfare schemes like old-age pensions, disability benefits, and employment guarantee schemes like MNREGA.",
            "keywords": "41 work job old age sick disable pension welfare assistance mnrega benefit",
            "link": LINK_PART_4,
            "student_view": "🎓 **Student:** Basis for scholarship schemes for the needy.",
            "nri_view": "🌍 **NRI:** N/A.",
            "gov_emp_view": "🏛️ **Gov Employee:** You implement pension and welfare schemes under this.",
            "pvt_emp_view": "💼 **Private Employee:** Relates to social security benefits like PF/Gratuity.",
            "politician_view": "🗳️ **Politician:** MNREGA (Right to Work) is based on this.",
            "ngo_view": "🤝 **NGO:** Fight for rights of the elderly and disabled."
        },
        {
            "article_number": "Article 44",
            "part": "Part IV - Directive Principles",
            "text": "Uniform Civil Code.",
            "explanation": "Article 44 states that the State shall endeavor to secure for the citizens a Uniform Civil Code (UCC) throughout the territory of India. Currently, different religions have different personal laws (marriage, divorce, inheritance). A UCC would mean a common set of civil laws for all citizens, regardless of religion, promoting national integration and gender justice.",
            "keywords": "44 ucc uniform civil code marriage divorce law common personal law inheritance",
            "link": LINK_PART_4,
            "student_view": "🎓 **Student:** A debated topic about having common family laws for all.",
            "nri_view": "🌍 **NRI:** Changes in marriage/inheritance laws affect your property in India.",
            "gov_emp_view": "🏛️ **Gov Employee:** If implemented, admin processes for marriage registration will unify.",
            "pvt_emp_view": "💼 **Private Employee:** Standardizes inheritance rules for employees.",
            "politician_view": "🗳️ **Politician:** A major policy debate; know your stance.",
            "ngo_view": "🤝 **NGO:** Monitor impact on gender justice and minority rights."
        },
        {
            "article_number": "Article 51A",
            "part": "Part IV-A - Fundamental Duties",
            "text": "It shall be the duty of every citizen to abide by the Constitution...",
            "explanation": "Article 51A lists the Fundamental Duties of every citizen. These include: abiding by the Constitution, respecting the National Flag and Anthem, protecting the sovereignty of India, defending the country, promoting harmony, protecting the environment, and safeguarding public property. While rights are what you get, duties are what you owe to the nation.",
            "keywords": "51a duties duty citizen flag anthem environment property vandalism respect harmony",
            "link": LINK_PART_4A,
            "student_view": "🎓 **Student:** Respect public property and strive for excellence.",
            "nri_view": "🌍 **NRI:** You still carry the duty to represent India with dignity.",
            "gov_emp_view": "🏛️ **Gov Employee:** Your service is a fulfillment of these duties.",
            "pvt_emp_view": "💼 **Private Employee:** Corporate Social Responsibility (CSR) aligns here.",
            "politician_view": "🗳️ **Politician:** Lead by example in upholding these duties.",
            "ngo_view": "🤝 **NGO:** Work in environment/social reform applies Art 51A."
        },
        {
            "article_number": "Article 326",
            "part": "Part XV - Elections",
            "text": "Elections to the House of the People... on basis of adult suffrage.",
            "explanation": "Article 326 guarantees the Right to Vote (Adult Suffrage). It states that elections to the Lok Sabha and State Assemblies shall be on the basis of adult suffrage. This means every citizen who is not less than 18 years of age has the right to vote without discrimination on grounds of religion, race, caste, or sex.",
            "keywords": "326 vote election 18 adult suffrage democracy voter card id polling",
            "link": LINK_PART_15,
            "student_view": "🎓 **Student:** If you are 18, get your Voter ID. It's your power.",
            "nri_view": "🌍 **NRI:** You can vote (often in person), but rules are evolving for e-voting.",
            "gov_emp_view": "🏛️ **Gov Employee:** You conduct these elections (Election Duty).",
            "pvt_emp_view": "💼 **Private Employee:** Paid leave on voting day is your right.",
            "politician_view": "🗳️ **Politician:** Your entire career depends on this article!",
            "ngo_view": "🤝 **NGO:** Voter awareness campaigns are crucial here."
        },
        {
            "article_number": "Article 361",
            "part": "Part XIX - Miscellaneous",
            "text": "Protection of President and Governors.",
            "explanation": "Article 361 provides immunity to the President and Governors. They are not answerable to any court for the exercise of their official duties. Furthermore, no criminal proceedings can be instituted or continued against them during their term of office, and they cannot be arrested or imprisoned while in office.",
            "keywords": "361 president governor immunity court arrest case suit",
            "link": "https://www.mea.gov.in/Images/pdf1/Part19.pdf",
            "student_view": "🎓 **Student:** Civics fact: The President cannot be arrested while in office.",
            "nri_view": "🌍 **NRI:** N/A",
            "gov_emp_view": "🏛️ **Gov Employee:** You work in the name of the President/Governor.",
            "pvt_emp_view": "💼 **Private Employee:** N/A",
            "politician_view": "🗳️ **Politician:** Understand the limits of executive immunity.",
            "ngo_view": "🤝 **NGO:** You cannot easily sue the Head of State, challenge the Govt instead."
        }
    ]

    cursor.executemany('''
        INSERT INTO articles (
            article_number, part, text, explanation, keywords, link,
            student_view, nri_view, gov_emp_view, pvt_emp_view, politician_view, ngo_view
        )
        VALUES (
            :article_number, :part, :text, :explanation, :keywords, :link,
            :student_view, :nri_view, :gov_emp_view, :pvt_emp_view, :politician_view, :ngo_view
        )
    ''', articles)
    
    conn.commit()
    conn.close()
    print("Database REBUILT with Rich Content (5 lines) and Correct PDF Links!")

if __name__ == '__main__':
    init_db()