                            </a>
                            <button class="project-btn" onclick="showToast('Actively being built with exciting new social features!')">
                                <i class="fas fa-hammer"></i> Status
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Project 3: Custom Django REST APIs -->
                <div class="project-card glass-card" data-category="django">
                    <div class="project-banner" style="background: linear-gradient(135deg, #064e3b, #0f172a);">
                        <div class="project-mockup-code">
                            <div><span style="color: #34d399;">POST</span> /api/v1/auth/jwt/create</div>
                            <div style="color: #94a3b8;">{ "token": "Bearer eyJhbGciOi...", "status": 200 }</div>
                            <div style="margin-top: 5px;"><span style="color: #60a5fa;">GET</span> /api/v1/dashboard/metrics</div>
                            <div style="color: #fbbf24;">[ { "cached": true, "response_time": "12ms" } ]</div>
                        </div>
                        <span class="project-badge-tag"><i class="fas fa-shield-alt"></i> Secure API</span>
                    </div>

                    <div class="project-content">
                        <h3 class="project-title">Custom Django REST APIs & Services</h3>
                        <p class="project-desc">
                            High-performance backend API services equipped with JWT authentication, role-based access control (RBAC), and automated endpoint documentation.
                        </p>

                        <ul class="project-highlights">
                            <li><i class="fas fa-check-circle"></i> JWT Token generation, refresh, and granular permission handling.</li>
                            <li><i class="fas fa-check-circle"></i> Optimized PostgreSQL queries with select_related & prefetch_related.</li>
                            <li><i class="fas fa-check-circle"></i> Clean, maintainable endpoints ready for mobile and web consumption.</li>
                        </ul>

                        <div class="project-tags">
                            <span class="tag-pill">Django REST Framework</span>
                            <span class="tag-pill">JWT</span>
                            <span class="tag-pill">PostgreSQL</span>
                            <span class="tag-pill">Linux</span>
                        </div>

                        <div class="project-footer">
                            <a href="https://github.com/sajwin-code" target="_blank" rel="noopener noreferrer" class="project-btn">
                                <i class="fab fa-github"></i> Explore Code
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 4: Digital Creative & UI/UX Systems -->
                <div class="project-card glass-card" data-category="creative">
                    <div class="project-banner" style="background: linear-gradient(135deg, #4c1d95, #0f172a);">
                        <div class="project-mockup-code">
                            <div><span style="color: #c084fc;">FigmaDesignSystem</span> {</div>
                            <div style="padding-left: 15px;">components: <span style="color: #60a5fa;">"Glassmorphic UI Kit"</span>;</div>
                            <div style="padding-left: 15px;">video_editing: <span style="color: #34d399;">"Adobe Premiere Pro"</span>;</div>
                            <div style="padding-left: 15px;">graphics: <span style="color: #fbbf24;">"Photoshop & Lightroom"</span>;</div>
                            <div>}</div>
                        </div>
                        <span class="project-badge-tag"><i class="fas fa-pen-nib"></i> Design & Media</span>
                    </div>

                    <div class="project-content">
                        <h3 class="project-title">UI/UX Design & Creative Media Works</h3>
                        <p class="project-desc">
                            A curated suite of modern user interface prototypes in Figma, digital graphic branding, photo enhancement, and high-impact promo video editing.
                        </p>

                        <ul class="project-highlights">
                            <li><i class="fas fa-check-circle"></i> Intuitive wireframes and high-fidelity prototypes in Figma & Canva.</li>
                            <li><i class="fas fa-check-circle"></i> Visual branding and photo editing with Adobe Photoshop & Lightroom.</li>
                            <li><i class="fas fa-check-circle"></i> Video post-production with Adobe Premiere Pro.</li>
                        </ul>

                        <div class="project-tags">
                            <span class="tag-pill">Figma</span>
                            <span class="tag-pill">Photoshop</span>
                            <span class="tag-pill">Premiere Pro</span>
                            <span class="tag-pill">Lightroom</span>
                        </div>

                        <div class="project-footer">
                            <a href="#contact" class="project-btn">
                                <i class="fas fa-comments"></i> Inquire Creative Services
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. SERVICES SECTION -->
    <section class="section" id="services" style="background: var(--bg-secondary);">
        <div class="container">
            <div class="section-header">
                <span class="section-tag"><i class="fas fa-cogs"></i> What I Deliver</span>
                <h2 class="section-title">Tailored Web & <span class="gradient-text">Digital Services</span></h2>
                <p class="section-subtitle">Delivering high quality, scalable digital solutions from concept to production.</p>
            </div>

            <div class="services-grid">
                <!-- Service 1 -->
                <div class="service-card glass-card">
                    <div class="service-icon">
                        <i class="fas fa-laptop-code"></i>
                    </div>
                    <h3 class="service-title">Full-Stack Web Development</h3>
                    <p class="service-desc">
                        End-to-end custom web applications built with Python, Django, Svelte, and PostgreSQL. From responsive frontends to scalable databases.
                    </p>
                    <ul class="service-features">
                        <li><i class="fas fa-check"></i> Responsive layouts (Mobile/Desktop)</li>
                        <li><i class="fas fa-check"></i> Clean Django MVC/MVT structure</li>
                        <li><i class="fas fa-check"></i> Production-ready deployment</li>
                    </ul>
                </div>

                <!-- Service 2 -->
                <div class="service-card glass-card">
                    <div class="service-icon">
                        <i class="fas fa-server"></i>
                    </div>
                    <h3 class="service-title">RESTful API & Backend Engineering</h3>
                    <p class="service-desc">
                        Designing robust, secure, and well-documented REST APIs with Django REST Framework, JWT auth, and optimized PostgreSQL queries.
                    </p>
                    <ul class="service-features">
                        <li><i class="fas fa-check"></i> Secure Authentication & RBAC</li>
                        <li><i class="fas fa-check"></i> Database optimization & caching</li>
                        <li><i class="fas fa-check"></i> Third-party API integrations</li>
                    </ul>
                </div>

                <!-- Service 3 -->
# -*- coding: utf-8 -*-
"""
SAJWIN SHAKKEER BIN JAFFAR - SVELTE MASTER GENERATOR
"""
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def write_component(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path}")

portfolio_data = """export const personalInfo = {
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
    title: 'Django Enterprise Business Portal',
    category: 'fullstack python',
    badge: 'Full-Stack Django',
    description: 'Scalable multi-tenant business web application with role-based access control, PostgreSQL schema architecture, automated reports, and high-security authentication.',
    tags: ['Python', 'Django', 'PostgreSQL', 'Tailwind', 'Docker'],
    github: 'https://github.com/sajwin-code',
    demo: 'https://github.com/sajwin-code',
    icon: 'fas fa-building'
  },
  {
    id: 2,
    title: 'Svelte Reactive Analytics Platform',
    category: 'frontend svelte',
    badge: 'Svelte & Vite',
    description: 'High-performance interactive telemetry dashboard featuring real-time data visualizer, glassmorphic UI components, smooth canvas charts, and dark mode.',
    tags: ['Svelte', 'JavaScript', 'Canvas', 'Vite', 'CSS3'],
    github: 'https://github.com/sajwin-code',
    demo: 'https://github.com/sajwin-code',
    icon: 'fas fa-chart-line'
  },
  {
    id: 3,
    title: 'High-Throughput RESTful API Gateway',
    category: 'api python',
    badge: 'DRF & Microservices',
    description: 'Engineered robust token-authenticated RESTful API backend handling data validation, rate-limiting, Swagger documentation, and PostgreSQL connection pooling.',
    tags: ['Django REST', 'Python', 'JWT', 'Redis', 'Swagger'],
    github: 'https://github.com/sajwin-code',
    demo: 'https://github.com/sajwin-code',
    icon: 'fas fa-network-wired'
  },
  {
    id: 4,
    title: 'E-Commerce & Payment Integration Hub',
    category: 'fullstack python',
    badge: 'Full-Stack Web App',
    description: 'Custom e-commerce application featuring catalog management, cart logic, automated invoicing, and secure payment gateway integrations (Stripe / Razorpay).',
    tags: ['Django', 'Python', 'Stripe', 'PostgreSQL', 'JavaScript'],
    github: 'https://github.com/sajwin-code',
    demo: 'https://github.com/sajwin-code',
    icon: 'fas fa-shopping-cart'
  },
  {
    id: 5,
    title: 'AI Multilingual Content Engine',
    category: 'api python',
    badge: 'AI & Backend',
    description: 'Natural language pipeline leveraging modern LLM APIs to generate and localize content seamlessly across Arabic, English, Urdu, Hindi, and Malayalam.',
    tags: ['Python', 'FastAPI', 'OpenAI API', 'Celery', 'Redis'],
    github: 'https://github.com/sajwin-code',
    demo: 'https://github.com/sajwin-code',
    icon: 'fas fa-robot'
  },
  {
    id: 6,
    title: 'Interactive 3D Canvas Globe Portfolio',
    category: 'frontend svelte',
    badge: 'Creative Engineering',
    description: 'Svelte 3D orthographic spherical planet renderer with solid landmass shading, direct-manipulation inertia physics, and responsive theme support.',
    tags: ['Svelte', 'HTML5 Canvas', 'Math & 3D', 'Vite'],
    github: 'https://github.com/sajwin-code',
    demo: 'https://github.com/sajwin-code',
    icon: 'fas fa-globe-americas'
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
"""
write_component("src/data/portfolioData.js", portfolio_data)

# 2. src/components/Navbar.svelte
navbar_svelte = """<script>
  import { onMount } from 'svelte';
  import { theme, toggleTheme } from '../stores/theme.js';
  import { personalInfo } from '../data/portfolioData.js';

  let isScrolled = false;
  let isMobileOpen = false;
  let activeSection = 'home';

  const navLinks = [
    { href: '#home', label: 'Home' },
    { href: '#about', label: 'About' },
    { href: '#languages', label: 'Languages' },
    { href: '#skills', label: 'Skills' },
    { href: '#projects', label: 'Projects' },
    { href: '#pricing', label: 'Pricing' },
    { href: '#services', label: 'Services' },
    { href: '#contact', label: 'Contact' }
  ];

  function handleScroll() {
    const scrollY = window.pageYOffset;
    isScrolled = scrollY > 50;

    const sections = document.querySelectorAll('section[id]');
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        activeSection = sectionId;
      }
    });
  }

  function toggleMobile() { isMobileOpen = !isMobileOpen; }
  function closeMobile() { isMobileOpen = false; }

  onMount(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

<header class="navbar" class:scrolled={isScrolled} id="navbar">
  <div class="container nav-container">
    <a href="#home" class="nav-logo">
      <span class="logo-symbol">S</span>
      <span>Sajwin<span class="gradient-text">.dev</span></span>
    </a>

    <nav class="nav-links">
      {#each navLinks as link}
        <a 
          href={link.href} 
          class="nav-link" 
          class:active={activeSection === link.href.substring(1)}
        >
          {link.label}
        </a>
      {/each}
    </nav>

    <div class="nav-actions">
      <button class="theme-toggle" on:click={toggleTheme} aria-label="Toggle Dark/Light Theme">
        <i class={$theme === 'light' ? 'fas fa-moon' : 'fas fa-sun'}></i>
      </button>

      <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn-fiverr-nav" title="Hire on Fiverr">
        <i class="fas fa-bolt"></i> Fiverr
      </a>

      <a href="#contact" class="btn-nav">
        <i class="fas fa-paper-plane"></i> Let's Talk
      </a>

      <button class="mobile-menu-btn" on:click={toggleMobile} aria-label="Toggle Menu">
        <i class={isMobileOpen ? 'fas fa-times' : 'fas fa-bars'}></i>
      </button>
    </div>
  </div>

  <div class="mobile-nav" class:open={isMobileOpen}>
    {#each navLinks as link}
      <a 
        href={link.href} 
        class="nav-link" 
        class:active={activeSection === link.href.substring(1)}
        on:click={closeMobile}
      >
        {link.label}
      </a>
    {/each}
    <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn-nav" style="margin-top: 0.5rem; justify-content: center;">
      <i class="fas fa-bolt"></i> Fiverr Profile (@sajwin_sj)
    </a>
  </div>
</header>

<style>
  .btn-fiverr-nav {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.48rem 0.95rem;
    border-radius: var(--radius-full);
    font-size: 0.85rem;
    font-weight: 700;
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
    transition: var(--transition);
  }
  .btn-fiverr-nav:hover {
    background: #10b981;
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
    transform: translateY(-2px);
  }
</style>
"""
write_component("src/components/Navbar.svelte", navbar_svelte)

# 3. src/components/Hero.svelte
hero_svelte = """<script>
  import { onMount } from 'svelte';
  import { personalInfo } from '../data/portfolioData.js';

  let currentText = '';
  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  const phrases = personalInfo.roleTitles;

  function handleTyping() {
    const currentPhrase = phrases[phraseIndex];
    if (isDeleting) {
      currentText = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
    } else {
      currentText = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
    }

    let speed = isDeleting ? 45 : 85;

    if (!isDeleting && charIndex === currentPhrase.length) {
      speed = 2000;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      speed = 350;
    }

    setTimeout(handleTyping, speed);
  }

  onMount(() => {
    setTimeout(handleTyping, 600);
  });
</script>

<section class="hero" id="home">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <div class="status-badge">
          <span class="pulse-dot"></span>
          Available for Freelance & Full-Time Roles
        </div>

        <h1 class="hero-title">
          Hi, I'm <span class="gradient-text">{personalInfo.shortName} Shakkeer</span><br>Bin Jaffar
        </h1>

        <div class="typing-wrapper">
          <span id="typing-text">{currentText}</span><span class="typing-cursor"></span>
        </div>

        <p class="hero-description">
          Full-Stack Developer and BCA scholar at <strong>Manipal University Jaipur</strong> with expertise in <strong>Python, Django, Svelte, PostgreSQL</strong>, and modern AI-driven engineering. Combining clean backend architecture with intuitive UI/UX and native multilingual proficiency.
        </p>

        <div class="hero-cta">
          <a href="#projects" class="btn btn-primary btn-glow">
            <i class="fas fa-code-branch"></i> View Featured Projects
          </a>
          <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn btn-fiverr">
            <i class="fas fa-bolt"></i> Hire on Fiverr
          </a>
          <a href="#contact" class="btn btn-outline">
            <i class="fas fa-envelope"></i> Contact Me
          </a>
          <a href="mailto:sajwinshakkeer@gmail.com?subject=Resume%20Request%20-%20Sajwin%20Shakkeer" class="btn btn-outline" title="Request Official Resume">
            <i class="fas fa-file-alt"></i> Request CV
          </a>
        </div>

        <div class="hero-socials">
          <a href={personalInfo.github} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="GitHub Profile" title="GitHub (@sajwin-code)">
            <i class="fab fa-github"></i>
          </a>
          <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="social-icon-btn fiverr-social" aria-label="Fiverr Profile" title="Fiverr (@sajwin_sj)">
            <span class="fiverr-txt">fi</span>
          </a>
          <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="LinkedIn Profile" title="LinkedIn">
            <i class="fab fa-linkedin-in"></i>
          </a>
          <a href="mailto:sajwinshakkeer@gmail.com" class="social-icon-btn" aria-label="Email Me" title="Email">
            <i class="fas fa-envelope"></i>
          </a>
          <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="WhatsApp Contact" title="WhatsApp">
            <i class="fab fa-whatsapp"></i>
          </a>
        </div>
      </div>

      <div class="hero-media">
        <div class="hero-media-wrapper">
          <img src={personalInfo.avatar} alt="{personalInfo.name} - Full Stack Developer" class="hero-banner-img" />
          
          <div class="floating-tech-badge-right">
            <i class="fab fa-python badge-icon"></i>
            <div>
              <div class="badge-text-title">Backend Specialist</div>
              <div class="badge-text-val">Django & DRF APIs</div>
            </div>
          </div>

          <div class="floating-tech-badge">
            <i class="fas fa-globe-americas badge-icon"></i>
            <div>
              <div class="badge-text-title">Global Communicator</div>
              <div class="badge-text-val">7 Languages Fluent</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .btn-fiverr {
    background: linear-gradient(135deg, #10b981, #059669);
    color: #ffffff;
    border: none;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
  }
  .btn-fiverr:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
  }
  .fiverr-social {
    background: rgba(16, 185, 129, 0.15);
    border-color: rgba(16, 185, 129, 0.3);
    color: #10b981;
  }
  .fiverr-social:hover {
    background: #10b981;
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
  }
  .fiverr-txt {
    font-weight: 900;
    font-family: sans-serif;
    font-size: 1.1rem;
    line-height: 1;
  }
</style>
"""
write_component("src/components/Hero.svelte", hero_svelte)

# 4. src/components/Stats.svelte
stats_svelte = """<script>
  import { onMount } from 'svelte';
  import { statsData } from '../data/portfolioData.js';

  let currentCounts = statsData.map(() => 0);
  let hasAnimated = false;
  let sectionElement;

  function animate() {
    if (hasAnimated || !sectionElement) return;
    const rect = sectionElement.getBoundingClientRect();
    if (rect.top <= window.innerHeight * 0.88) {
      hasAnimated = true;
      statsData.forEach((stat, i) => {
        let current = 0;
        const target = stat.target;
        const increment = Math.ceil(target / 35);
        const timer = setInterval(() => {
          current += increment;
          if (current >= target) {
            currentCounts[i] = target;
            clearInterval(timer);
          } else {
            currentCounts[i] = current;
          }
        }, 35);
      });
    }
  }

  onMount(() => {
    window.addEventListener('scroll', animate, { passive: true });
    animate();
    return () => window.removeEventListener('scroll', animate);
  });
</script>

<section class="stats-section" bind:this={sectionElement}>
  <div class="container">
    <div class="stats-grid">
      {#each statsData as stat, index}
        <div class="stat-card glass-card">
          <div class="stat-number">{currentCounts[index]}{stat.suffix}</div>
          <div class="stat-label">{stat.label}</div>
        </div>
      {/each}
    </div>
  </div>
</section>
"""
write_component("src/components/Stats.svelte", stats_svelte)

# 5. src/components/About.svelte
about_svelte = """<script>
  import { personalInfo } from '../data/portfolioData.js';
</script>

<section class="about-section" id="about">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-user"></i> About & Academics</span>
      <h2 class="section-title">Bridging Code, Architecture & <span class="gradient-text">Global Context</span></h2>
      <p class="section-subtitle">A synthesis of formal Computer Science foundations, hands-on production web engineering, and multilingual communication.</p>
    </div>

    <div class="about-grid">
      <div class="about-bio-card glass-card">
        <h3 class="about-card-title"><i class="fas fa-compass"></i> Engineering Philosophy</h3>
        <p class="about-p">
          I specialize in architecting scalable, maintainable, and high-throughput web applications with <strong>Python, Django, PostgreSQL, and Svelte</strong>. I focus on clean backend models, robust API contracts, and responsive, accessible user interfaces.
        </p>
        <p class="about-p">
          Being fluent in <strong>7 languages</strong> enables me to communicate effortlessly with global engineering teams, cross-functional stakeholders, and international clients across the Americas, Europe, Middle East, and South Asia.
        </p>

        <div class="about-highlights-grid">
          <div class="about-highlight-box">
            <i class="fas fa-server highlight-icon"></i>
            <div>
              <div class="highlight-title">Backend Specialist</div>
              <div class="highlight-desc">Django, DRF APIs & PostgreSQL</div>
            </div>
          </div>
          <div class="about-highlight-box">
            <i class="fas fa-bolt highlight-icon"></i>
            <div>
              <div class="highlight-title">Modern Frontend</div>
              <div class="highlight-desc">Svelte, Vite & Reactive State</div>
            </div>
          </div>
          <div class="about-highlight-box">
            <i class="fas fa-shield-alt highlight-icon"></i>
            <div>
              <div class="highlight-title">Clean Architecture</div>
              <div class="highlight-desc">Security, Caching & Modular Code</div>
            </div>
          </div>
          <div class="about-highlight-box">
            <i class="fas fa-handshake highlight-icon"></i>
            <div>
              <div class="highlight-title">Global Freelance</div>
              <div class="highlight-desc">Verified Fiverr Seller (@sajwin_sj)</div>
            </div>
          </div>
        </div>
      </div>

      <div class="about-edu-column">
        <div class="edu-card glass-card">
          <div class="edu-header">
            <div class="edu-icon"><i class="fas fa-graduation-cap"></i></div>
            <div>
              <div class="edu-tag">Undergraduate Degree</div>
              <h3 class="edu-title">{personalInfo.degree}</h3>
              <div class="edu-institution">{personalInfo.university}</div>
            </div>
          </div>
          <p class="edu-desc">
            Rigorous university curriculum covering Data Structures & Algorithms, Database Management Systems (RDBMS), Object-Oriented Software Design, Web Technologies, and Computer Networks.
          </p>
        </div>

        <div class="edu-card glass-card">
          <div class="edu-header">
            <div class="edu-icon"><i class="fas fa-laptop-code"></i></div>
            <div>
              <div class="edu-tag">Senior Secondary</div>
              <h3 class="edu-title">Computer Science & Mathematics</h3>
              <div class="edu-institution">{personalInfo.schooling}</div>
            </div>
          </div>
          <p class="edu-desc">
            Early foundational training in computational logic, algorithm design, Python programming fundamentals, and discrete mathematics.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write_component("src/components/About.svelte", about_svelte)

# 6. src/components/Globe.svelte
globe_svelte = """<script>
  import { onMount } from 'svelte';
  import { theme } from '../stores/theme.js';
  import { languagesData } from '../data/portfolioData.js';
  import { WORLD_LAND_POLYGONS } from '../data/worldData.js';

  let canvas;
  let activeLang = languagesData[0];
  let isDragging = false;
  let hoveredFlag = null;

  let yaw = -75 * Math.PI / 180;
  let pitch = 15 * Math.PI / 180;
  let targetYaw = yaw;
  let targetPitch = pitch;
  let isTransitioning = false;
  let velYaw = 0;
  let velPitch = 0;
  let lastMouseX = 0;
  let lastMouseY = 0;
  let pulseTime = 0;

  function selectLanguage(lang) {
    activeLang = lang;
    targetYaw = lang.lon * Math.PI / 180;
    targetPitch = Math.max(-0.4, Math.min(0.5, lang.lat * Math.PI / 180 * 0.45));
    isTransitioning = true;
    velYaw = 0;
    velPitch = 0;
  }

  onMount(() => {
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animId;

    let width = 480;
    let height = 480;
    let radius = 175;
    let dpr = window.devicePixelRatio || 1;

    function resize() {
      const rect = canvas.getBoundingClientRect();
      width = rect.width || 480;
      height = rect.height || 480;
      dpr = window.devicePixelRatio || 1;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      radius = Math.min(width, height) * 0.36;
    }
    resize();
    window.addEventListener('resize', resize);

    const graticuleLines = [];
    for (let lat = -60; lat <= 60; lat += 30) {
      const pts = [];
      for (let lon = -180; lon <= 180; lon += 8) pts.push({ lat, lon });
      graticuleLines.push(pts);
    }
    for (let lon = -180; lon < 180; lon += 45) {
      const pts = [];
      for (let lat = -80; lat <= 80; lat += 6) pts.push({ lat, lon });
      graticuleLines.push(pts);
    }

    function project(lat, lon, heightOffset = 0) {
      const radLat = lat * Math.PI / 180;
      const radLon = lon * Math.PI / 180;
      const r = radius + heightOffset;

      const cosLat = Math.cos(radLat);
      const sinLat = Math.sin(radLat);
      const deltaLon = radLon - yaw;

      const x0 = cosLat * Math.sin(deltaLon);
      const y0 = sinLat;
      const z0 = cosLat * Math.cos(deltaLon);

      const cosPitch = Math.cos(pitch);
      const sinPitch = Math.sin(pitch);

      const x = x0;
      const y = y0 * cosPitch - z0 * sinPitch;
      const z = y0 * sinPitch + z0 * cosPitch;

      const cx = (width * dpr) / 2;
      const cy = (height * dpr) / 2;

      return {
        x: cx + x * r * dpr,
        y: cy - y * r * dpr,
        z: z,
        visible: z > -0.15
      };
    }

    const onMouseDown = (e) => {
      isDragging = true;
      isTransitioning = false;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
      velYaw = 0;
      velPitch = 0;
    };

    const onMouseUp = () => { isDragging = false; };

    const onMouseMove = (e) => {
      const rect = canvas.getBoundingClientRect();
      const mouseX = (e.clientX - rect.left) * dpr;
      const mouseY = (e.clientY - rect.top) * dpr;

      if (isDragging) {
        const dx = e.clientX - lastMouseX;
        const dy = e.clientY - lastMouseY;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;

        velYaw = dx * 0.006;
        velPitch = dy * 0.006;

        yaw -= velYaw;
        pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
      } else {
        let found = null;
        let minDist = Infinity;

        languagesData.forEach(lang => {
          const pHeight = lang.poleHeight || 32;
          const surface = project(lang.lat, lang.lon, 0);
          const tip = project(lang.lat, lang.lon, pHeight);

          if (surface.visible && surface.z > -0.1) {
            const offX = (lang.offsetX || 0) * dpr;
            const offY = (lang.offsetY || 0) * dpr;
            const targetX = tip.x + offX;
            const targetY = tip.y + offY;

            const dist = Math.hypot(mouseX - targetX, mouseY - targetY);
            if (dist < 32 * dpr && dist < minDist) {
              minDist = dist;
              found = lang;
            }
          }
        });

        if (found) {
          canvas.style.cursor = 'pointer';
          if (hoveredFlag !== found) {
            hoveredFlag = found;
            activeLang = found;
          }
        } else {
          canvas.style.cursor = isDragging ? 'grabbing' : 'grab';
          hoveredFlag = null;
        }
      }
    };

    const onTouchStart = (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        isTransitioning = false;
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;
        velYaw = 0;
        velPitch = 0;
      }
    };

    const onTouchMove = (e) => {
      if (isDragging && e.touches.length === 1) {
        const dx = e.touches[0].clientX - lastMouseX;
        const dy = e.touches[0].clientY - lastMouseY;
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;

        velYaw = dx * 0.007;
        velPitch = dy * 0.007;

        yaw -= velYaw;
        pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
      }
    };

    const onTouchEnd = () => { isDragging = false; };

    canvas.addEventListener('mousedown', onMouseDown);
    window.addEventListener('mouseup', onMouseUp);
    canvas.addEventListener('mousemove', onMouseMove);
    canvas.addEventListener('touchstart', onTouchStart, { passive: true });
    canvas.addEventListener('touchmove', onTouchMove, { passive: true });
    canvas.addEventListener('touchend', onTouchEnd);

    function render() {
      pulseTime += 0.04;

      if (isTransitioning) {
        let diffYaw = targetYaw - yaw;
        while (diffYaw < -Math.PI) diffYaw += Math.PI * 2;
        while (diffYaw > Math.PI) diffYaw -= Math.PI * 2;

        yaw += diffYaw * 0.08;
        pitch += (targetPitch - pitch) * 0.08;

        if (Math.abs(diffYaw) < 0.002 && Math.abs(targetPitch - pitch) < 0.002) {
          yaw = targetYaw;
          pitch = targetPitch;
          isTransitioning = false;
        }
      } else if (!isDragging && !hoveredFlag) {
        if (Math.abs(velYaw) > 0.0005) {
          yaw -= velYaw;
          velYaw *= 0.94;
        } else {
          yaw -= 0.0025;
        }

        if (Math.abs(velPitch) > 0.0005) {
          pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
          velPitch *= 0.94;
        }
      }

      const isLight = $theme === 'light';
      const globeBg = isLight ? '#eef2f6' : '#0b111e';
      const graticuleColor = isLight ? 'rgba(100, 116, 139, 0.08)' : 'rgba(148, 163, 184, 0.06)';
      const ringBorder = isLight ? 'rgba(96, 165, 250, 0.25)' : 'rgba(56, 189, 248, 0.2)';
      const landFill = isLight ? '#cbd5e1' : '#1e293b';
      const landStroke = isLight ? 'rgba(100, 116, 139, 0.35)' : 'rgba(96, 165, 250, 0.35)';

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = (width * dpr) / 2;
      const cy = (height * dpr) / 2;
      const rScaled = radius * dpr;

      // 1. Ocean Sphere
      ctx.save();
      ctx.beginPath();
      ctx.arc(cx, cy, rScaled, 0, Math.PI * 2);
      ctx.fillStyle = globeBg;
      ctx.fill();

      const innerGrad = ctx.createRadialGradient(cx - rScaled * 0.3, cy - rScaled * 0.3, rScaled * 0.1, cx, cy, rScaled);
      if (isLight) {
        innerGrad.addColorStop(0, 'rgba(255, 255, 255, 0.7)');
        innerGrad.addColorStop(0.7, 'rgba(238, 242, 246, 0.85)');
        innerGrad.addColorStop(1, 'rgba(203, 213, 225, 0.5)');
      } else {
        innerGrad.addColorStop(0, 'rgba(24, 38, 64, 0.35)');
        innerGrad.addColorStop(0.7, 'rgba(11, 17, 30, 0.9)');
        innerGrad.addColorStop(1, 'rgba(6, 10, 18, 0.98)');
      }
      ctx.fillStyle = innerGrad;
      ctx.fill();

      ctx.lineWidth = 1.2 * dpr;
      ctx.strokeStyle = ringBorder;
      ctx.stroke();
      ctx.restore();

      // 2. Solid Vector Landmasses
      if (WORLD_LAND_POLYGONS && WORLD_LAND_POLYGONS.length > 0) {
        ctx.save();
        ctx.beginPath();
        ctx.arc(cx, cy, rScaled - 0.5 * dpr, 0, Math.PI * 2);
        ctx.clip();

        WORLD_LAND_POLYGONS.forEach(ring => {
          let started = false;
          ctx.beginPath();
          for (let i = 0; i < ring.length; i++) {
            const p = project(ring[i][0], ring[i][1], 0);
            if (p.visible && p.z > -0.05) {
              if (!started) {
                ctx.moveTo(p.x, p.y);
                started = true;
              } else {
                ctx.lineTo(p.x, p.y);
              }
            } else {
              started = false;
            }
          }
          ctx.fillStyle = landFill;
          ctx.fill();
          ctx.strokeStyle = landStroke;
          ctx.lineWidth = 1 * dpr;
          ctx.stroke();
        });
        ctx.restore();
      }

      // 3. Graticules
      ctx.save();
      ctx.lineWidth = 1 * dpr;
      ctx.strokeStyle = graticuleColor;
      graticuleLines.forEach(line => {
        ctx.beginPath();
        let isDrawing = false;
        line.forEach(pt => {
          const proj = project(pt.lat, pt.lon, 0);
          if (proj.visible && proj.z > 0) {
            if (!isDrawing) { ctx.moveTo(proj.x, proj.y); isDrawing = true; }
            else { ctx.lineTo(proj.x, proj.y); }
          } else { isDrawing = false; }
        });
        ctx.stroke();
      });
      ctx.restore();

      // 4. Sticking-out Flagpoles & Badges
      const projectedFlags = languagesData.map(lang => {
        const pHeight = lang.poleHeight || 32;
        const surface = project(lang.lat, lang.lon, 0);
        const tip = project(lang.lat, lang.lon, pHeight);
        const offX = (lang.offsetX || 0) * dpr;
        const offY = (lang.offsetY || 0) * dpr;
        return {
          lang,
          surface,
          tip,
          badgeCenter: { x: tip.x + offX, y: tip.y + offY },
          isActive: lang.id === activeLang.id,
          isHovered: hoveredFlag && hoveredFlag.id === lang.id
        };
      }).sort((a, b) => {
        if (a.isHovered || a.isActive) return 1;
        if (b.isHovered || b.isActive) return -1;
        return a.surface.z - b.surface.z;
      });

      projectedFlags.forEach(({ lang, surface, tip, badgeCenter, isActive, isHovered }) => {
        if (!surface.visible || surface.z < -0.1) return;

        const opacity = Math.max(0.2, Math.min(1, (surface.z + 0.1) * 2));
        ctx.save();
        ctx.globalAlpha = opacity;

        // Anchor Dot
        ctx.beginPath();
        ctx.arc(surface.x, surface.y, (isActive || isHovered ? 4 : 2.8) * dpr, 0, Math.PI * 2);
        ctx.fillStyle = isLight ? '#0284c7' : '#38bdf8';
        ctx.fill();

        if (isActive || isHovered) {
          ctx.beginPath();
          const pulseR = (5.5 + Math.sin(pulseTime * 3) * 2.5) * dpr;
          ctx.arc(surface.x, surface.y, pulseR, 0, Math.PI * 2);
          ctx.strokeStyle = isLight ? 'rgba(2, 132, 199, 0.45)' : 'rgba(56, 189, 248, 0.45)';
          ctx.lineWidth = 1.2 * dpr;
          ctx.stroke();
        }

        // Stem Line
        ctx.beginPath();
        ctx.moveTo(surface.x, surface.y);
        ctx.lineTo(tip.x, tip.y);
        if (badgeCenter.x !== tip.x || badgeCenter.y !== tip.y) {
          ctx.lineTo(badgeCenter.x, badgeCenter.y);
        }
        ctx.lineWidth = (isActive || isHovered ? 1.8 : 1.2) * dpr;
        const poleGrad = ctx.createLinearGradient(surface.x, surface.y, badgeCenter.x, badgeCenter.y);
        if (isLight) {
          poleGrad.addColorStop(0, '#0284c7');
          poleGrad.addColorStop(1, '#0d9488');
        } else {
          poleGrad.addColorStop(0, 'rgba(96, 165, 250, 0.7)');
          poleGrad.addColorStop(1, 'rgba(45, 212, 191, 0.85)');
        }
        ctx.strokeStyle = poleGrad;
        ctx.stroke();

        // Flag Badge
        const pillText = `${lang.flag} ${lang.name.split(' ')[0]}`;
        ctx.font = `600 ${Math.round(11 * dpr)}px sans-serif`;
        const textW = ctx.measureText(pillText).width;
        const padX = 8 * dpr;
        const padY = 4 * dpr;
        const pillW = textW + padX * 2;
        const pillH = 22 * dpr;
        const pillX = badgeCenter.x - pillW / 2;
        const pillY = badgeCenter.y - pillH / 2;

        ctx.beginPath();
        ctx.roundRect(pillX, pillY, pillW, pillH, 11 * dpr);

        if (isActive || isHovered) {
          ctx.fillStyle = isLight ? '#ffffff' : '#1e293b';
          ctx.fill();
          ctx.strokeStyle = isLight ? '#0284c7' : '#38bdf8';
          ctx.lineWidth = 1.8 * dpr;
          ctx.stroke();
          ctx.shadowColor = isLight ? 'rgba(2, 132, 199, 0.3)' : 'rgba(56, 189, 248, 0.35)';
          ctx.shadowBlur = 8 * dpr;
        } else {
          ctx.fillStyle = isLight ? 'rgba(255, 255, 255, 0.95)' : 'rgba(17, 24, 39, 0.9)';
          ctx.fill();
          ctx.strokeStyle = isLight ? 'rgba(0, 0, 0, 0.1)' : 'rgba(255, 255, 255, 0.12)';
          ctx.lineWidth = 1 * dpr;
          ctx.stroke();
        }

        ctx.shadowBlur = 0;
        ctx.fillStyle = isLight ? '#0f172a' : '#f1f5f9';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(pillText, badgeCenter.x, badgeCenter.y);
        ctx.restore();
      });

      animId = requestAnimationFrame(render);
    }

    render();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener('resize', resize);
      window.removeEventListener('mouseup', onMouseUp);
      if (canvas) {
        canvas.removeEventListener('mousedown', onMouseDown);
        canvas.removeEventListener('mousemove', onMouseMove);
        canvas.removeEventListener('touchstart', onTouchStart);
        canvas.removeEventListener('touchmove', onTouchMove);
        canvas.removeEventListener('touchend', onTouchEnd);
      }
    };
  });
</script>

<section class="polyglot-section" id="languages">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-globe-americas"></i> Polyglot Advantage</span>
      <h2 class="section-title">Global Reach Across <span class="gradient-text">7 Languages</span></h2>
      <p class="section-subtitle">Interact with the 3D globe to explore language proficiency, native greetings, and cultural hubs.</p>
    </div>

    <div class="globe-layout">
      <div class="globe-visual-wrapper glass-card">
        <div class="globe-container">
          <div class="globe-atmosphere"></div>
          <canvas bind:this={canvas} id="globe-canvas" width="600" height="600"></canvas>
          <div class="globe-instruction-tag">
            <i class="fas fa-arrows-alt"></i> <span>Drag to rotate globe • Hover flags to explore</span>
          </div>
        </div>
      </div>

      <div class="globe-sidebar">
        <div class="globe-detail-card glass-card" id="globe-detail-card">
          <div class="detail-header">
            <div class="detail-flag-badge">{activeLang.flag}</div>
            <div>
              <h3 class="detail-lang-name">{activeLang.name}</h3>
              <span class="detail-level-tag {activeLang.levelClass}">{activeLang.level}</span>
            </div>
            <span class="detail-region-tag"><i class="fas fa-map-marker-alt"></i> {activeLang.region}</span>
          </div>

          <div class="detail-greeting-display">
            <div class="detail-script-title">Native Greeting</div>
            <div class="detail-greeting-script" class:rtl={activeLang.isRTL}>{activeLang.greeting}</div>
            <div class="detail-greeting-translit">{activeLang.translit}</div>
          </div>

          <p class="detail-desc">{activeLang.desc}</p>
        </div>

        <div class="globe-lang-selector-title">
          <i class="fas fa-compass"></i> Focus Language Location
        </div>
        <div class="globe-lang-pills">
          {#each languagesData as lang}
            <button 
              class="globe-pill" 
              class:active={activeLang.id === lang.id}
              on:click={() => selectLanguage(lang)}
            >
              <span>{lang.flag} {lang.name.split(' ')[0]}</span>
              <span class="pill-badge">{lang.level}</span>
            </button>
          {/each}
        </div>
      </div>
    </div>
  </div>
</section>
"""
write_component("src/components/Globe.svelte", globe_svelte)

# 7. src/components/Skills.svelte
skills_svelte = """<script>
  import { skillsData } from '../data/portfolioData.js';
</script>

<section class="skills-section" id="skills">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-code"></i> Technical Stack</span>
      <h2 class="section-title">Skills & Modern <span class="gradient-text">Capabilities Matrix</span></h2>
      <p class="section-subtitle">Deep expertise across modern full-stack web technologies, relational architecture, and clean developer workflows.</p>
    </div>

    <div class="skills-categories">
      {#each skillsData as cat}
        <div class="skill-category-card glass-card">
          <div class="category-header">
            <div class="category-icon"><i class={cat.icon}></i></div>
            <h3 class="category-title">{cat.category}</h3>
          </div>
          <div class="skills-list">
            {#each cat.items as skill}
              <div class="skill-item">
                <div class="skill-info">
                  <span class="skill-name"><i class="{skill.icon} skill-icon"></i> {skill.name}</span>
                  <span class="skill-percentage">{skill.level}%</span>
                </div>
                <div class="skill-progress-bar">
                  <div class="skill-progress-fill" style="width: {skill.level}%;"></div>
                </div>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
"""
write_component("src/components/Skills.svelte", skills_svelte)

# 8. src/components/Projects.svelte
projects_svelte = """<script>
  import { projectsData } from '../data/portfolioData.js';

  let currentFilter = 'all';

  const filterTabs = [
    { key: 'all', label: 'All Projects' },
    { key: 'fullstack', label: 'Full-Stack' },
    { key: 'python', label: 'Python & Django' },
    { key: 'svelte', label: 'Svelte' },
    { key: 'api', label: 'APIs & AI' }
  ];

  $: filteredProjects = currentFilter === 'all'
    ? projectsData
    : projectsData.filter(p => p.category.includes(currentFilter));
</script>

<section class="projects-section" id="projects">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-layer-group"></i> Portfolio Showcase</span>
      <h2 class="section-title">Featured Engineering <span class="gradient-text">Projects</span></h2>
      <p class="section-subtitle">Selected production web apps, RESTful microservices, and reactive user interfaces built with modern toolchains.</p>
    </div>

    <div class="projects-filter-wrapper">
      {#each filterTabs as tab}
        <button 
          class="filter-btn" 
          class:active={currentFilter === tab.key}
          on:click={() => currentFilter = tab.key}
        >
          {tab.label}
        </button>
      {/each}
    </div>

    <div class="projects-grid">
      {#each filteredProjects as proj (proj.id)}
        <div class="project-card glass-card">
          <div class="project-header">
            <div class="project-icon-box"><i class={proj.icon}></i></div>
            <span class="project-badge">{proj.badge}</span>
          </div>

          <h3 class="project-title">{proj.title}</h3>
          <p class="project-description">{proj.description}</p>

          <div class="project-tags">
            {#each proj.tags as tag}
              <span class="tech-tag">{tag}</span>
            {/each}
          </div>

          <div class="project-links">
            <a href={proj.github} target="_blank" rel="noopener noreferrer" class="btn-proj btn-proj-primary">
              <i class="fab fa-github"></i> Repository
            </a>
            <a href={proj.demo} target="_blank" rel="noopener noreferrer" class="btn-proj btn-proj-secondary">
              <i class="fas fa-external-link-alt"></i> Details
            </a>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
"""
write_component("src/components/Projects.svelte", projects_svelte)

# 9. src/components/Services.svelte
services_svelte = """<script>
  import { servicesData } from '../data/portfolioData.js';
</script>

<section class="services-section" id="services">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-cogs"></i> Offerings</span>
      <h2 class="section-title">Development & Architectural <span class="gradient-text">Services</span></h2>
      <p class="section-subtitle">Comprehensive software development capabilities from concept and database modeling to deployment and scaling.</p>
    </div>

    <div class="services-grid">
      {#each servicesData as srv}
        <div class="service-card glass-card">
          <div class="service-icon"><i class={srv.icon}></i></div>
          <h3 class="service-title">{srv.title}</h3>
          <p class="service-desc">{srv.description}</p>
          <ul class="service-deliverables">
            {#each srv.deliverables as del}
              <li><i class="fas fa-check-circle check-icon"></i> {del}</li>
            {/each}
          </ul>
        </div>
      {/each}
    </div>
  </div>
</section>
"""
write_component("src/components/Services.svelte", services_svelte)

# 10. src/components/Pricing.svelte
pricing_svelte = """<script>
  import { currency, toggleCurrency } from '../stores/currency.js';
  import { pricingPackages, comparisonMatrix, personalInfo } from '../data/portfolioData.js';

  let showComparison = false;

  function toggleComparisonTable() {
    showComparison = !showComparison;
  }
</script>

<section class="pricing-section" id="pricing">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-tag"></i> Packages & Pricing</span>
      <h2 class="section-title">Transparent Plans & <span class="gradient-text">Development Packages</span></h2>
      <p class="section-subtitle">Secure freelance orders backed by Fiverr Escrow Buyer Protection. Custom scopes also available upon request.</p>
    </div>

    <!-- Currency Switcher -->
    <div class="currency-toggle-wrapper">
      <span class="currency-label" class:active={$currency === 'INR'}>₹ INR (India)</span>
      <button class="currency-switch-btn" on:click={toggleCurrency} aria-label="Switch Currency">
        <span class="currency-thumb" class:usd={$currency === 'USD'}></span>
      </button>
      <span class="currency-label" class:active={$currency === 'USD'}>$ USD (Global)</span>
    </div>

    <!-- Pricing Cards Grid -->
    <div class="pricing-grid">
      {#each pricingPackages as pkg}
        <div class="pricing-card glass-card" class:popular={pkg.popular}>
          {#if pkg.popular}
            <div class="popular-badge"><i class="fas fa-fire"></i> Most Popular</div>
          {/if}

          <div class="package-tier-name">{pkg.name}</div>
          <h3 class="package-title">{pkg.title}</h3>
          <p class="package-desc">{pkg.description}</p>

          <div class="package-price-box">
            <span class="price-starting-tag">Starting from</span>
            <div class="price-val">
              {#if $currency === 'INR'}
                <span class="currency-sym">₹</span>{pkg.priceINR.toLocaleString('en-IN')}
              {:else}
                <span class="currency-sym">$</span>{pkg.priceUSD}
              {/if}
            </div>
          </div>

          <div class="package-meta-badges">
            <div class="meta-badge"><i class="fas fa-clock"></i> {pkg.deliveryDays} Days Delivery</div>
            <div class="meta-badge"><i class="fas fa-sync-alt"></i> {pkg.revisions} Revisions</div>
            <div class="meta-badge"><i class="fas fa-file-code"></i> {pkg.pages} Pages</div>
          </div>

          <ul class="package-features-list">
            {#each pkg.features as feat}
              <li class:excluded={!feat.included}>
                <i class={feat.included ? "fas fa-check-circle feat-check" : "fas fa-minus-circle feat-cross"}></i>
                <span>{feat.text}</span>
              </li>
            {/each}
          </ul>

          <a href={pkg.fiverrLink} target="_blank" rel="noopener noreferrer" class="btn btn-package" class:btn-primary={pkg.popular} class:btn-outline={!pkg.popular}>
            <i class="fas fa-bolt"></i> Order on Fiverr
          </a>
        </div>
      {/each}
    </div>

    <!-- Comparison Table Accordion Toggle -->
    <div class="comparison-toggle-box">
      <button class="btn btn-outline" on:click={toggleComparisonTable}>
        <i class={showComparison ? "fas fa-chevron-up" : "fas fa-table"}></i>
        {showComparison ? "Hide Detailed Comparison Matrix" : "View Full Feature Comparison Table"}
      </button>
    </div>

    {#if showComparison}
      <div class="comparison-table-wrapper glass-card">
        <table class="comparison-table">
          <thead>
            <tr>
              <th class="th-feature">Package Deliverables</th>
              <th class="th-tier">BASIC<br><span class="th-price">{$currency === 'INR' ? '₹6,999' : '$80'}</span></th>
              <th class="th-tier popular-col">STANDARD<br><span class="th-price">{$currency === 'INR' ? '₹14,999' : '$180'}</span></th>
              <th class="th-tier">PREMIUM<br><span class="th-price">{$currency === 'INR' ? '₹29,999' : '$350'}</span></th>
            </tr>
          </thead>
          <tbody>
            {#each comparisonMatrix as row}
              <tr>
                <td class="td-feature">{row.feature}</td>
                
                <td class="td-val">
                  {#if typeof row.basic === 'boolean'}
                    <i class={row.basic ? "fas fa-check-circle table-check" : "fas fa-minus table-minus"}></i>
                  {:else}
                    <span class="table-text">{row.basic}</span>
                  {/if}
                </td>

                <td class="td-val popular-col">
                  {#if typeof row.standard === 'boolean'}
                    <i class={row.standard ? "fas fa-check-circle table-check" : "fas fa-minus table-minus"}></i>
                  {:else}
                    <span class="table-text">{row.standard}</span>
                  {/if}
                </td>

                <td class="td-val">
                  {#if typeof row.premium === 'boolean'}
                    <i class={row.premium ? "fas fa-check-circle table-check" : "fas fa-minus table-minus"}></i>
                  {:else}
                    <span class="table-text">{row.premium}</span>
                  {/if}
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}

    <!-- Fiverr Escrow Trust Banner -->
    <div class="fiverr-trust-banner glass-card">
      <div class="trust-content">
        <div class="trust-icon"><i class="fas fa-shield-alt"></i></div>
        <div>
          <h4 class="trust-title">Secure Milestone Orders via Fiverr Escrow</h4>
          <p class="trust-p">Payments are safely held in escrow by Fiverr and only released upon your 100% satisfaction and delivery approval.</p>
        </div>
      </div>
      <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn btn-fiverr-trust">
        <i class="fas fa-external-link-alt"></i> Visit @sajwin_sj on Fiverr
      </a>
    </div>
  </div>
</section>

<style>
  .pricing-section {
    background: var(--bg-secondary);
    position: relative;
  }
  .currency-toggle-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
  }
  .currency-label {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-muted);
    transition: var(--transition);
  }
  .currency-label.active {
    color: var(--primary);
  }
  .currency-switch-btn {
    width: 58px;
    height: 32px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    position: relative;
    cursor: pointer;
    padding: 3px;
    transition: var(--transition);
  }
  .currency-thumb {
    display: block;
    width: 24px;
    height: 24px;
    background: var(--primary);
    border-radius: 50%;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .currency-thumb.usd {
    transform: translateX(26px);
  }
  .pricing-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-bottom: 2.5rem;
    align-items: stretch;
  }
  .pricing-card {
    padding: 2.25rem 2rem;
    display: flex;
    flex-direction: column;
    position: relative;
    border-radius: var(--radius-lg);
    transition: var(--transition);
  }
  .pricing-card.popular {
    border-color: var(--primary);
    box-shadow: 0 8px 30px var(--primary-glow);
    transform: scale(1.03);
    z-index: 2;
  }
  .popular-badge {
    position: absolute;
    top: -14px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: #ffffff;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 0.35rem 1rem;
    border-radius: var(--radius-full);
    box-shadow: 0 4px 12px var(--primary-glow);
  }
  .package-tier-name {
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--primary);
    margin-bottom: 0.5rem;
  }
  .package-title {
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 0.75rem;
    color: var(--text-primary);
  }
  .package-desc {
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 1.5rem;
    min-height: 48px;
  }
  .package-price-box {
    margin-bottom: 1.5rem;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid var(--border-color);
  }
  .price-starting-tag {
    font-size: 0.75rem;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--text-muted);
    display: block;
    margin-bottom: 0.25rem;
  }
  .price-val {
    font-size: 2.4rem;
    font-weight: 900;
    color: var(--text-primary);
    font-family: var(--font-heading);
    line-height: 1.1;
  }
  .currency-sym {
    font-size: 1.6rem;
    color: var(--primary);
    margin-right: 2px;
  }
  .package-meta-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
  .meta-badge {
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.25rem 0.65rem;
    border-radius: var(--radius-sm);
    background: var(--bg-main);
    color: var(--text-secondary);
    border: 1px solid var(--border-color);
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
  }
  .package-features-list {
    list-style: none;
    margin-bottom: 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    flex-grow: 1;
  }
  .package-features-list li {
    font-size: 0.88rem;
    display: flex;
    align-items: center;
    gap: 0.65rem;
    color: var(--text-primary);
  }
  .package-features-list li.excluded {
    color: var(--text-muted);
    opacity: 0.65;
  }
  .feat-check { color: #10b981; }
  .feat-cross { color: var(--text-muted); opacity: 0.6; }
  .btn-package {
    width: 100%;
    justify-content: center;
  }
  .comparison-toggle-box {
    text-align: center;
    margin-bottom: 2rem;
  }
  .comparison-table-wrapper {
    overflow-x: auto;
    padding: 1.5rem;
    border-radius: var(--radius-lg);
    margin-bottom: 2.5rem;
  }
  .comparison-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
  }
  .comparison-table th, .comparison-table td {
    padding: 1rem 1.25rem;
    border-bottom: 1px solid var(--border-color);
  }
  .th-feature, .td-feature {
    text-align: left;
    font-weight: 600;
    color: var(--text-primary);
  }
  .th-tier, .td-val {
    text-align: center;
    width: 22%;
  }
  .th-price {
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--primary);
  }
  .popular-col {
    background: rgba(56, 189, 248, 0.04);
  }
  .table-check { color: #10b981; font-size: 1.1rem; }
  .table-minus { color: var(--text-muted); opacity: 0.5; }
  .table-text { font-weight: 700; color: var(--text-primary); }
  .fiverr-trust-banner {
    padding: 1.75rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    flex-wrap: wrap;
    border-radius: var(--radius-lg);
  }
  .trust-content {
    display: flex;
    align-items: center;
    gap: 1.25rem;
  }
  .trust-icon {
    font-size: 2.2rem;
    color: #10b981;
  }
  .trust-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
  }
  .trust-p {
    font-size: 0.88rem;
    color: var(--text-secondary);
  }
  .btn-fiverr-trust {
    background: #10b981;
    color: #ffffff;
    padding: 0.75rem 1.5rem;
    font-weight: 700;
    border-radius: var(--radius-full);
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: var(--transition);
  }
  .btn-fiverr-trust:hover {
    background: #059669;
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
    transform: translateY(-2px);
  }
  @media (max-width: 1024px) {
    .pricing-grid {
      grid-template-columns: 1fr;
    }
    .pricing-card.popular {
      transform: none;
    }
  }
</style>
"""
write_component("src/components/Pricing.svelte", pricing_svelte)

# 11. src/components/Contact.svelte
contact_svelte = """<script>
  import { personalInfo } from '../data/portfolioData.js';
  import { showToast, copyToClipboard } from '../stores/toast.js';

  let name = '';
  let email = '';
  let subject = '';
  let message = '';

  function handleSubmit(e) {
    e.preventDefault();
    if (!name || !email || !message) {
      showToast('Please fill out all required fields.');
      return;
    }

    const sub = subject || 'Project Inquiry / Message';
    const mailtoUrl = `mailto:${personalInfo.email}?subject=${encodeURIComponent(sub)}&body=${encodeURIComponent(`Name: ${name}\\nEmail: ${email}\\n\\nMessage:\\n${message}`)}`;
    window.location.href = mailtoUrl;

    showToast('Opening your email client to send message...');
    name = ''; email = ''; subject = ''; message = '';
  }
</script>

<section class="contact-section" id="contact">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-paper-plane"></i> Get In Touch</span>
      <h2 class="section-title">Let's Build Something <span class="gradient-text">Extraordinary</span></h2>
      <p class="section-subtitle">Whether you need a custom Django backend, a lightning-fast Svelte interface, or full-stack consulting, I'm ready to collaborate.</p>
    </div>

    <div class="contact-grid">
      <!-- Contact Details -->
      <div class="contact-info-panel glass-card">
        <h3 class="contact-panel-title"><i class="fas fa-address-card"></i> Contact Details</h3>
        <p class="contact-panel-desc">Reach out directly via email, WhatsApp, or order a verified escrow gig on Fiverr.</p>

        <div class="contact-methods">
          <div class="contact-method-item">
            <div class="method-icon"><i class="fas fa-envelope"></i></div>
            <div class="method-details">
              <span class="method-label">Direct Email</span>
              <a href="mailto:{personalInfo.email}" class="method-val">{personalInfo.email}</a>
            </div>
            <button class="copy-btn" on:click={() => copyToClipboard(personalInfo.email, 'Email')} title="Copy Email" aria-label="Copy Email">
              <i class="far fa-copy"></i>
            </button>
          </div>

          <div class="contact-method-item">
            <div class="method-icon"><i class="fab fa-whatsapp"></i></div>
            <div class="method-details">
              <span class="method-label">WhatsApp / Phone</span>
              <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="method-val">{personalInfo.phone}</a>
            </div>
            <button class="copy-btn" on:click={() => copyToClipboard(personalInfo.phone, 'Phone Number')} title="Copy Phone" aria-label="Copy Phone">
              <i class="far fa-copy"></i>
            </button>
          </div>

          <div class="contact-method-item">
            <div class="method-icon"><i class="fas fa-bolt" style="color: #10b981;"></i></div>
            <div class="method-details">
              <span class="method-label">Fiverr Profile</span>
              <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="method-val">fiverr.com/{personalInfo.fiverrUsername}</a>
            </div>
          </div>

          <div class="contact-method-item">
            <div class="method-icon"><i class="fas fa-map-marker-alt"></i></div>
            <div class="method-details">
              <span class="method-label">Location</span>
              <span class="method-val">{personalInfo.location}</span>
            </div>
          </div>
        </div>

        <div class="contact-availability-box">
          <span class="avail-dot"></span>
          <span>Open for freelance contracts, full-time positions, and technical partnerships.</span>
        </div>
      </div>

      <!-- Contact Form -->
      <div class="contact-form-panel glass-card">
        <h3 class="contact-panel-title"><i class="fas fa-envelope-open-text"></i> Send a Message</h3>
        <form on:submit={handleSubmit} class="contact-form" id="contact-form">
          <div class="form-group">
            <label for="form-name" class="form-label">Your Name *</label>
            <input type="text" id="form-name" class="form-input" placeholder="e.g. Alex Morgan" bind:value={name} required />
          </div>

          <div class="form-group">
            <label for="form-email" class="form-label">Your Email *</label>
            <input type="email" id="form-email" class="form-input" placeholder="e.g. alex@company.com" bind:value={email} required />
          </div>

          <div class="form-group">
            <label for="form-subject" class="form-label">Subject</label>
            <input type="text" id="form-subject" class="form-input" placeholder="e.g. Web App Development Project" bind:value={subject} />
          </div>

          <div class="form-group">
            <label for="form-message" class="form-label">Message *</label>
            <textarea id="form-message" class="form-textarea" placeholder="Tell me about your project scope, requirements, or timeline..." bind:value={message} required></textarea>
          </div>

          <button type="submit" class="btn btn-primary btn-glow" style="width: 100%; justify-content: center;">
            <i class="fas fa-paper-plane"></i> Send Message Directly
          </button>
        </form>
      </div>
    </div>
  </div>
</section>
"""
write_component("src/components/Contact.svelte", contact_svelte)

# 12. src/components/Toast.svelte
toast_svelte = """<script>
  import { toast } from '../stores/toast.js';
</script>

<div class="toast-container" class:show={$toast.visible} id="toast">
  <i class="fas fa-check-circle"></i>
  <span id="toast-message">{$toast.message}</span>
</div>
"""
write_component("src/components/Toast.svelte", toast_svelte)

# 13. src/components/BackToTop.svelte
backtotop_svelte = """<script>
  import { onMount } from 'svelte';

  let visible = false;

  function handleScroll() {
    visible = window.pageYOffset > 400;
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  onMount(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

<button 
  class="back-to-top" 
  class:visible={visible} 
  on:click={scrollToTop} 
  aria-label="Back to Top" 
  title="Back to Top"
>
  <i class="fas fa-chevron-up"></i>
</button>
"""
write_component("src/components/BackToTop.svelte", backtotop_svelte)

# 14. src/components/Footer.svelte
footer_svelte = """<script>
  import { personalInfo } from '../data/portfolioData.js';
</script>

<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <a href="#home" class="nav-logo">
          <span class="logo-symbol">S</span>
          <span>Sajwin<span class="gradient-text">.dev</span></span>
        </a>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem; max-width: 320px;">
          Full-Stack Web Developer, Python Specialist & Multilingual Creator.
        </p>
      </div>

      <div class="hero-socials">
        <a href={personalInfo.github} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="GitHub">
          <i class="fab fa-github"></i>
        </a>
        <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="Fiverr" title="Fiverr">
          <span style="font-weight: 900; font-size: 1rem;">fi</span>
        </a>
        <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="LinkedIn">
          <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="mailto:{personalInfo.email}" class="social-icon-btn" aria-label="Email">
          <i class="fas fa-envelope"></i>
        </a>
        <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="WhatsApp">
          <i class="fab fa-whatsapp"></i>
        </a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>
        &copy; 2026 {personalInfo.name}. All rights reserved.
      </div>
      <div>
        Engineered with <i class="fas fa-heart" style="color: #ef4444;"></i> using Svelte 5, Python, Django & Vite.
      </div>
    </div>
  </div>
</footer>
"""
write_component("src/components/Footer.svelte", footer_svelte)

# 15. src/App.svelte
app_svelte = """<script>
  import Navbar from './components/Navbar.svelte';
  import Hero from './components/Hero.svelte';
  import Stats from './components/Stats.svelte';
  import About from './components/About.svelte';
  import Globe from './components/Globe.svelte';
  import Skills from './components/Skills.svelte';
  import Projects from './components/Projects.svelte';
  import Pricing from './components/Pricing.svelte';
  import Services from './components/Services.svelte';
  import Contact from './components/Contact.svelte';
  import Footer from './components/Footer.svelte';
  import Toast from './components/Toast.svelte';
  import BackToTop from './components/BackToTop.svelte';
</script>

<div class="app-root">
  <Navbar />
  <main>
    <Hero />
    <Stats />
    <About />
    <Globe />
    <Skills />
    <Projects />
    <Pricing />
    <Services />
    <Contact />
  </main>
  <Footer />
  <Toast />
  <BackToTop />
</div>

<style>
  .app-root {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  main {
    flex: 1;
  }
</style>
"""
write_component("src/App.svelte", app_svelte)

print("\nALL SVELTE COMPONENTS GENERATED SUCCESSFULLY!")
