export const personalInfo = {
  name: 'Sajwin Shakkeer Bin Jaffar',
  shortName: 'Sajwin',
  title: 'Full-Stack Developer | Python Specialist | Multilingual Polyglot',
  roleTitles: [
    'Full-Stack Developer',
    'Python & Django Specialist',
    'Svelte & Modern Web Engineer',
    'Multilingual Polyglot (7 Languages)',
    'Digital & UI/UX Creator'
  ],
  bio: 'Full-Stack Developer and BCA scholar at Manipal University Jaipur with expertise in Python, Django, Svelte, PostgreSQL, and modern AI-driven engineering. Combining clean backend architecture with intuitive UI/UX and native multilingual proficiency.',
  degree: 'Bachelor of Computer Applications (BCA)',
  university: 'Manipal University Jaipur',
  schooling: 'Senior Secondary (Computer Science), NIOS',
  email: 'sajwinshakkeer@gmail.com',
  phone: '+91 9496908306',
  whatsapp: 'https://wa.me/919496908306',
  location: 'Kannur, Kerala, India',
  website: 'https://sajwinshakkeers.in/',
  github: 'https://github.com/sajwin-code',
  githubUsername: 'sajwin-code',
  linkedin: 'https://www.linkedin.com/in/sajwin',
  fiverr: 'https://www.fiverr.com/sajwin_sj',
  fiverrUsername: 'sajwin_sj',
  avatar: 'assets/images/sajwin-portrait.jpg',
  profileImg: 'assets/images/sajwin-profile.png'
};

export const statsData = [
  { target: 7, suffix: '+', label: 'Languages Spoken' },
  { target: 10, suffix: '+', label: 'Tech Stacks & Tools' },
  { target: 100, suffix: '%', label: 'Responsive & Scalable Code' },
  { target: 1, suffix: 'st', label: 'BCA @ Manipal Univ Jaipur' }
];

export const languagesData = [
  {
    id: 'malayalam',
    name: 'Malayalam (മലയാളം)',
    flag: '🇮🇳',
    lat: 11.87,
    lon: 75.37,
    poleHeight: 32,
    offsetX: -4,
    offsetY: 8,
    level: 'Native',
    levelClass: 'level-native',
    greeting: 'സ്വാഗതം',
    translit: '"Swagatham" — Welcome (Mother Tongue)',
    region: 'Kannur, Kerala, India',
    desc: 'Native mother tongue spoken with complete cultural fluency, rooted in Kannur, Kerala, India.',
    isRTL: false
  },
  {
    id: 'english',
    name: 'English',
    flag: '🇬🇧',
    lat: 51.50,
    lon: -0.12,
    poleHeight: 50,
    offsetX: -22,
    offsetY: -12,
    level: 'Fluent',
    levelClass: 'level-fluent',
    greeting: 'Welcome',
    translit: '"Welcome" — Global Professional Language',
    region: 'Global & International',
    desc: 'Primary language for software development, technical documentation, and international teams.',
    isRTL: false
  },
  {
    id: 'arabic',
    name: 'Arabic (العربية)',
    flag: '🇸🇦',
    lat: 24.71,
    lon: 46.67,
    poleHeight: 34,
    offsetX: 0,
    offsetY: 0,
    level: 'Expert',
    levelClass: 'level-expert',
    greeting: 'أهلاً وسهلاً',
    translit: '"Ahlan wa Sahlan" — A Warm & Generous Welcome',
    region: 'Middle East / Gulf Region',
    desc: 'Expert linguistic and written fluency, enabling deep engagement across Middle Eastern clients.',
    isRTL: true
  },
  {
    id: 'urdu',
    name: 'Urdu (اردو)',
    flag: '🇵🇰',
    lat: 31.52,
    lon: 74.35,
    poleHeight: 26,
    offsetX: -20,
    offsetY: 2,
    level: 'Fluent',
    levelClass: 'level-fluent',
    greeting: 'خوش آمدید',
    translit: '"Khush Aamdeed" — Welcome with Joy',
    region: 'South Asia',
    desc: 'Fluent verbal articulation, literary appreciation, and cross-cultural communication in South Asia.',
    isRTL: true
  },
  {
    id: 'hindi',
    name: 'Hindi (हिन्दी)',
    flag: '🇮🇳',
    lat: 28.61,
    lon: 77.20,
    poleHeight: 46,
    offsetX: 18,
    offsetY: -10,
    level: 'Fluent',
    levelClass: 'level-fluent',
    greeting: 'नमस्ते',
    translit: '"Namaste" — Greetings & Mutual Respect',
    region: 'India (National)',
    desc: 'Fluent national language proficiency for inter-state communication and pan-India collaboration.',
    isRTL: false
  },
  {
    id: 'spanish',
    name: 'Spanish (Español)',
    flag: '🇪🇸',
    lat: 40.41,
    lon: -3.70,
    poleHeight: 34,
    offsetX: -16,
    offsetY: 10,
    level: 'Beginner',
    levelClass: 'level-beginner',
    greeting: '¡Hola! Bienvenidos',
    translit: '"Hola! Bienvenidos" — Hello & Welcome',
    region: 'Spain & Latin America',
    desc: 'Active conversational vocabulary connecting with European and Latin American opportunities.',
    isRTL: false
  },
  {
    id: 'french',
    name: 'French (Français)',
    flag: '🇫🇷',
    lat: 48.85,
    lon: 2.35,
    poleHeight: 22,
    offsetX: 22,
    offsetY: 10,
    level: 'Beginner',
    levelClass: 'level-beginner',
    greeting: 'Bienvenue',
    translit: '"Bienvenue" — Welcome in French',
    region: 'France & Francophone World',
    desc: 'Elementary conversational proficiency, exploring opportunities across the Francophone world.',
    isRTL: false
  }
];

export const skillsData = [
  {
    category: 'Backend & APIs',
    icon: 'fas fa-server',
    items: [
      { name: 'Python', level: 95, icon: 'fab fa-python' },
      { name: 'Django & DRF', level: 92, icon: 'fas fa-cube' },
      { name: 'PostgreSQL', level: 88, icon: 'fas fa-database' },
      { name: 'Redis & Caching', level: 82, icon: 'fas fa-bolt' },
      { name: 'REST APIs & JWT', level: 94, icon: 'fas fa-network-wired' }
    ]
  },
  {
    category: 'Frontend & UI/UX',
    icon: 'fas fa-laptop-code',
    items: [
      { name: 'Svelte & SvelteKit', level: 90, icon: 'fas fa-fire' },
      { name: 'JavaScript (ES6+)', level: 92, icon: 'fab fa-js' },
      { name: 'HTML5 & CSS3', level: 96, icon: 'fab fa-html5' },
      { name: 'Tailwind CSS', level: 90, icon: 'fab fa-css3-alt' },
      { name: 'Responsive UI/UX', level: 94, icon: 'fas fa-mobile-alt' }
    ]
  },
  {
    category: 'Database & DevOps',
    icon: 'fas fa-layer-group',
    items: [
      { name: 'SQL & Database Design', level: 90, icon: 'fas fa-database' },
      { name: 'Git & GitHub', level: 92, icon: 'fab fa-git-alt' },
      { name: 'Docker Containers', level: 80, icon: 'fab fa-docker' },
      { name: 'Linux & Bash', level: 85, icon: 'fab fa-linux' },
      { name: 'Cloud & Hosting', level: 84, icon: 'fas fa-cloud' }
    ]
  },
  {
    category: 'Engineering & Architecture',
    icon: 'fas fa-brain',
    items: [
      { name: 'System Architecture', level: 88, icon: 'fas fa-project-diagram' },
      { name: 'Security & Auth', level: 90, icon: 'fas fa-shield-alt' },
      { name: 'Performance Optimization', level: 92, icon: 'fas fa-tachometer-alt' },
      { name: 'AI & API Integrations', level: 86, icon: 'fas fa-robot' },
      { name: 'Clean Code & SOLID', level: 94, icon: 'fas fa-check-double' }
    ]
  }
];

export const projectsData = [
  {
    id: 1,
    title: 'Polix — Modern E-Commerce Platform',
    name: 'Polix',
    status: 'Completed',
    statusClass: 'status-completed',
    category: 'fullstack python ecommerce',
    badge: 'Completed • Production-Ready',
    description: 'A full-featured, scalable full-stack e-commerce web application built with Python & Django. Features end-to-end product catalog management, category browsing, cart mechanics, secure checkout workflow, order management, and relational PostgreSQL architecture.',
    tags: ['Python', 'Django', 'PostgreSQL', 'JavaScript', 'HTML5/CSS3', 'E-Commerce'],
    github: 'https://github.com/sajwin-code/polix',
    demo: 'https://github.com/sajwin-code/polix',
    icon: 'fas fa-shopping-bag',
    highlights: [
      'Relational PostgreSQL schema for orders and inventory',
      'Cart management and checkout validation',
      'Modular Django apps with clean separation of concerns'
    ]
  },
  {
    id: 2,
    title: 'Syncora — Social Media Platform',
    name: 'Syncora',
    status: 'In Active Development',
    statusClass: 'status-wip',
    category: 'fullstack python social',
    badge: 'Work In Progress • Active on GitHub',
    description: 'A modern, full-stack social networking platform currently under active engineering. Designed for real-time community engagement, user profiles, interactive feeds, multimedia posts, and reactive user interactions.',
    tags: ['Python', 'Django', 'Svelte', 'PostgreSQL', 'Real-Time', 'In Progress'],
    github: 'https://github.com/sajwin-code/syncora',
    demo: 'https://github.com/sajwin-code/syncora',
    icon: 'fas fa-users',
    highlights: [
      'Active open-source repository on GitHub',
      'Real-time feed architecture and user interaction models',
      'Modern frontend coupled with Django backend'
    ]
  }
];

export const servicesData = [
  {
    title: 'Custom Web Application Development',
    icon: 'fas fa-code',
    description: 'End-to-end bespoke web apps built with Python, Django, and modern frontend tools. Designed from the ground up for speed, security, and scalability.',
    deliverables: ['Custom Backend Architecture', 'Responsive UI/UX', 'Database Modeling', 'API Integration']
  },
  {
    title: 'Modern Frontend & Svelte Interfaces',
    icon: 'fas fa-palette',
    description: 'Fast, reactive, and visually engaging single-page applications and interactive user interfaces with buttery smooth 60fps animations.',
    deliverables: ['Svelte Components', 'Glassmorphic Design', 'Mobile-First Layouts', 'High Lighthouse Scores']
  },
  {
    title: 'API Engineering & Backend Systems',
    icon: 'fas fa-server',
    description: 'Designing and documenting robust RESTful APIs, microservices, authentication systems (JWT/OAuth), and third-party webhook integrations.',
    deliverables: ['DRF / FastAPI Endpoints', 'Swagger / OpenAPI Docs', 'Secure Auth & Rate Limits', 'Database Optimization']
  },
  {
    title: 'Database Design & Cloud Deployment',
    icon: 'fas fa-cloud-upload-alt',
    description: 'Configuring relational databases (PostgreSQL/MySQL), caching with Redis, containerization with Docker, and seamless cloud server deployment.',
    deliverables: ['PostgreSQL Schema Design', 'Docker Containers', 'Linux Server Setup', 'CI/CD Automation']
  }
];

export const pricingPackages = [
  {
    id: 'basic',
    name: 'BASIC',
    title: 'Django Starter Web App',
    description: 'Custom Django web app with 3 pages, authentication, admin panel, and contact form.',
    priceUSD: 80,
    priceINR: 6999,
    deliveryDays: 5,
    revisions: 2,
    pages: 3,
    popular: false,
    badge: 'Starter Tier',
    features: [
      { text: 'Functional Website', included: true },
      { text: '3 Responsive Web Pages', included: true },
      { text: '2 Revision Cycles', included: true },
      { text: 'Content Upload Included', included: true },
      { text: '2 Plugins / Extensions Installed', included: true },
      { text: 'Opt-In / Lead Contact Form', included: true },
      { text: 'Social Media Integration', included: true },
      { text: 'Payment Gateway Integration', included: false },
      { text: 'Speed & SEO Optimization', included: false },
      { text: 'Hosting & Server Setup', included: false },
      { text: 'E-Commerce Functionality', included: false }
    ],
    fiverrLink: 'https://www.fiverr.com/sajwin_sj'
  },
  {
    id: 'standard',
    name: 'STANDARD',
    title: 'Django Business Web App',
    description: 'Custom Django web app with 5 pages, dashboard, payments, hosting, and optimization.',
    priceUSD: 180,
    priceINR: 14999,
    deliveryDays: 10,
    revisions: 5,
    pages: 5,
    popular: true,
    badge: 'Most Popular',
    features: [
      { text: 'Functional Website', included: true },
      { text: '5 Responsive Web Pages', included: true },
      { text: '5 Revision Cycles', included: true },
      { text: 'Content Upload Included', included: true },
      { text: '5 Plugins / Extensions Installed', included: true },
      { text: 'Payment Gateway (Stripe/Razorpay)', included: true },
      { text: 'Opt-In / Lead Contact Form', included: true },
      { text: 'Autoresponder Integration', included: true },
      { text: 'Speed & Code Optimization', included: true },
      { text: 'Hosting & Server Setup', included: true },
      { text: 'Social Media Integration', included: true }
    ],
    fiverrLink: 'https://www.fiverr.com/sajwin_sj'
  },
  {
    id: 'premium',
    name: 'PREMIUM',
    title: 'Advanced Django Web App',
    description: 'Complete custom Django web app with custom features, payments, deployment, and optimization.',
    priceUSD: 350,
    priceINR: 29999,
    deliveryDays: 14,
    revisions: 8,
    pages: 10,
    popular: false,
    badge: 'Enterprise Tier',
    features: [
      { text: 'Complete Functional Web Application', included: true },
      { text: '10 Responsive Custom Pages', included: true },
      { text: '8 Revision Cycles', included: true },
      { text: 'Content Upload Included', included: true },
      { text: '10 Plugins / Extensions Installed', included: true },
      { text: 'E-Commerce Functionality', included: true },
      { text: 'Payment Gateway Integration', included: true },
      { text: 'Opt-In & Autoresponder Setup', included: true },
      { text: 'Maximum Speed & SEO Tuning', included: true },
      { text: 'Production Hosting & Domain Setup', included: true },
      { text: 'Priority Dedicated Support', included: true }
    ],
    fiverrLink: 'https://www.fiverr.com/sajwin_sj'
  }
];

export const comparisonMatrix = [
  { feature: 'Functional website', basic: true, standard: true, premium: true },
  { feature: 'Number of pages', basic: '3', standard: '5', premium: '10' },
  { feature: 'Revisions', basic: '2', standard: '5', premium: '8' },
  { feature: 'Delivery timeline', basic: '5 Days', standard: '10 Days', premium: '14 Days' },
  { feature: 'Content upload', basic: true, standard: true, premium: true },
  { feature: 'Plugins/extensions installation', basic: '2', standard: '5', premium: '10' },
  { feature: 'E-commerce functionality', basic: false, standard: false, premium: true },
  { feature: 'Payment Integration', basic: false, standard: true, premium: true },
  { feature: 'Opt-In form', basic: true, standard: true, premium: true },
  { feature: 'Autoresponder Integration', basic: false, standard: true, premium: true },
  { feature: 'Speed optimization', basic: false, standard: true, premium: true },
  { feature: 'Hosting setup', basic: false, standard: true, premium: true },
  { feature: 'Social media icons', basic: true, standard: true, premium: true }
];
