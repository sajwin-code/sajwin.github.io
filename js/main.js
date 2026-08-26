/**
 * SAJWIN SHAKKEER BIN JAFFAR - PORTFOLIO INTERACTIVITY
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. THEME SWITCHER
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    
    // Check saved theme or system preference
    const savedTheme = localStorage.getItem('sajwin-theme') || 
        (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('sajwin-theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        if (theme === 'light') {
            themeIcon.className = 'fas fa-moon';
        } else {
            themeIcon.className = 'fas fa-sun';
        }
    }

    // 2. TYPING EFFECT
    const typingElement = document.getElementById('typing-text');
    const phrases = [
        'Full-Stack Developer',
        'Python & Django Specialist',
        'Svelte & Modern Web Engineer',
        'Multilingual Polyglot (7 Languages)',
        'Digital & UI/UX Creator'
    ];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 90;

    function typeEffect() {
        const currentPhrase = phrases[phraseIndex];
        
        if (isDeleting) {
            typingElement.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 45;
        } else {
            typingElement.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 90;
        }

        if (!isDeleting && charIndex === currentPhrase.length) {
            typingSpeed = 1800; // Pause at end of sentence
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            typingSpeed = 400; // Pause before typing new sentence
        }

        setTimeout(typeEffect, typingSpeed);
    }

    if (typingElement) {
        setTimeout(typeEffect, 600);
    }

    // 3. NAVBAR SCROLL & ACTIVE SPY
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    const backToTopBtn = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        const scrollY = window.pageYOffset;

        // Navbar shadow/blur increase on scroll
        if (scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Back to top visibility
        if (scrollY > 400) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }

        // Active link spy
        sections.forEach(current => {
            const sectionHeight = current.offsetHeight;
            const sectionTop = current.offsetTop - 120;
            const sectionId = current.getAttribute('id');

            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });

    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // 4. MOBILE MENU
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileNav = document.getElementById('mobile-nav');

    if (mobileMenuBtn && mobileNav) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileNav.classList.toggle('open');
            const icon = mobileMenuBtn.querySelector('i');
            if (mobileNav.classList.contains('open')) {
                icon.className = 'fas fa-times';
            } else {
                icon.className = 'fas fa-bars';
            }
        });

        // Close on clicking a link
        mobileNav.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileNav.classList.remove('open');
                mobileMenuBtn.querySelector('i').className = 'fas fa-bars';
            });
        });
    }

    // 5. PROJECT FILTERING
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filterValue === 'all' || category.includes(filterValue)) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // 6. STATS COUNTER ANIMATION
    const statsSection = document.querySelector('.stats-section');
    const statNumbers = document.querySelectorAll('.stat-number');
    let hasAnimatedStats = false;

    function animateStats() {
        if (!statsSection || hasAnimatedStats) return;

        const rect = statsSection.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.85) {
            statNumbers.forEach(stat => {
                const target = parseInt(stat.getAttribute('data-target'), 10);
                const suffix = stat.getAttribute('data-suffix') || '';
                let current = 0;
                const increment = Math.ceil(target / 40);
                
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        stat.textContent = target + suffix;
                        clearInterval(timer);
                    } else {
                        stat.textContent = current + suffix;
                    }
                }, 35);
            });
            hasAnimatedStats = true;
        }
    }

    window.addEventListener('scroll', animateStats);
    animateStats(); // In case already visible

    // 7. TOAST NOTIFICATION UTILITY
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');

    window.showToast = function(msg) {
        if (!toast || !toastMessage) return;
        toastMessage.textContent = msg;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3500);
    };

    // 8. COPY TO CLIPBOARD BUTTONS
    const copyBtns = document.querySelectorAll('.copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const textToCopy = btn.getAttribute('data-copy');
            if (navigator.clipboard) {
                navigator.clipboard.writeText(textToCopy).then(() => {
                    showToast(`Copied "${textToCopy}" to clipboard!`);
                });
            } else {
                const textArea = document.createElement('textarea');
                textArea.value = textToCopy;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                showToast(`Copied "${textToCopy}" to clipboard!`);
            }
        });
    });

    // 9. CONTACT FORM SUBMISSION HANDLER
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('form-name').value.trim();
            const email = document.getElementById('form-email').value.trim();
            const subject = document.getElementById('form-subject').value.trim() || 'Project Inquiry / Message';
            const message = document.getElementById('form-message').value.trim();

            if (!name || !email || !message) {
                showToast('Please fill out all required fields.');
                return;
            }

            // Open user's default email client prefilled
            const mailtoUrl = `mailto:sajwinshakkeer@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`)}`;
            window.location.href = mailtoUrl;

            showToast('Opening your email client to send message to Sajwin...');
            contactForm.reset();
        });
    }

    // --------------------------------------------------------------------------
    // 10. INTERACTIVE 3D ROTATABLE GLOBE ENGINE (60 FPS, ZERO LAG)
    // --------------------------------------------------------------------------
    function initGlobe() {
        const canvas = document.getElementById('globe-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        // Languages Data with staggered pole heights and offsets to prevent collision
        const languages = [
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
                desc: 'Primary language for software development, technical documentation, system design, and international engineering teams.',
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
                desc: 'Expert linguistic and written fluency, enabling deep engagement across Middle Eastern and GCC clients.',
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
                desc: 'Fluent verbal articulation, literary appreciation, and cross-cultural communication in South Asian communities.',
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
                desc: 'Fluent national language proficiency for inter-state communication and pan-India team collaboration.',
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
                desc: 'Actively expanding conversational vocabulary to connect with European and Latin American markets.',
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
                desc: 'Elementary conversational and reading proficiency in French, exploring global European opportunities.',
                isRTL: false
            }
        ];

        // UI elements
        const detailCard = document.getElementById('globe-detail-card');
        const detailFlag = document.getElementById('detail-flag');
        const detailName = document.getElementById('detail-name');
        const detailLevel = document.getElementById('detail-level');
        const detailRegion = document.getElementById('detail-region');
        const detailScript = document.getElementById('detail-script');
        const detailTranslit = document.getElementById('detail-translit');
        const detailDesc = document.getElementById('detail-desc');
        const pills = document.querySelectorAll('.globe-pill');

        let activeLangId = 'malayalam';

        function updateSidePanel(lang) {
            if (!lang) return;
            activeLangId = lang.id;

            if (detailFlag) detailFlag.textContent = lang.flag;
            if (detailName) detailName.textContent = lang.name;
            if (detailLevel) {
                detailLevel.textContent = lang.level;
                detailLevel.className = `detail-level-tag ${lang.levelClass}`;
            }
            if (detailRegion) detailRegion.innerHTML = `<i class="fas fa-map-marker-alt"></i> ${lang.region}`;
            if (detailScript) {
                detailScript.textContent = lang.greeting;
                if (lang.isRTL) {
                    detailScript.classList.add('rtl');
                } else {
                    detailScript.classList.remove('rtl');
                }
            }
            if (detailTranslit) detailTranslit.textContent = lang.translit;
            if (detailDesc) detailDesc.textContent = lang.desc;

            pills.forEach(p => {
                if (p.getAttribute('data-lang') === lang.id) {
                    p.classList.add('active');
                } else {
                    p.classList.remove('active');
                }
            });
        }

        // Generate geographic continent points
        const landPoints = [];
        const continentClusters = [
            // India & South Asia
            { minLat: 8, maxLat: 35, minLon: 68, maxLon: 90, density: 110 },
            // Middle East & Arabia
            { minLat: 12, maxLat: 36, minLon: 35, maxLon: 60, density: 70 },
            // Europe & UK
            { minLat: 36, maxLat: 62, minLon: -10, maxLon: 35, density: 120 },
            // Africa
            { minLat: -34, maxLat: 36, minLon: -15, maxLon: 50, density: 130 },
            // East & SE Asia
            { minLat: -10, maxLat: 50, minLon: 95, maxLon: 145, density: 130 },
            // North America
            { minLat: 15, maxLat: 65, minLon: -125, maxLon: -65, density: 140 },
            // South America
            { minLat: -55, maxLat: 12, minLon: -80, maxLon: -35, density: 100 },
            // Australia
            { minLat: -40, maxLat: -12, minLon: 112, maxLon: 154, density: 60 }
        ];

        // Seeded random for consistent land points
        let seed = 42;
        function rnd() {
            seed = (seed * 9301 + 49297) % 233280;
            return seed / 233280;
        }

        continentClusters.forEach(cluster => {
            for (let i = 0; i < cluster.density; i++) {
                const lat = cluster.minLat + (cluster.maxLat - cluster.minLat) * rnd();
                const lon = cluster.minLon + (cluster.maxLon - cluster.minLon) * rnd();
                landPoints.push({ lat, lon });
            }
        });

        // Add meridians / graticule rings
        const graticuleLines = [];
        // Parallels
        for (let lat = -60; lat <= 60; lat += 30) {
            const pts = [];
            for (let lon = -180; lon <= 180; lon += 8) {
                pts.push({ lat, lon });
            }
            graticuleLines.push(pts);
        }
        // Meridians
        for (let lon = -180; lon < 180; lon += 45) {
            const pts = [];
            for (let lat = -80; lat <= 80; lat += 6) {
                pts.push({ lat, lon });
            }
            graticuleLines.push(pts);
        }

        // Globe State
        let yaw = -75 * Math.PI / 180; // Start focused on India / South Asia
        let pitch = 15 * Math.PI / 180;
        let targetYaw = yaw;
        let targetPitch = pitch;
        let isTransitioningToTarget = false;

        let isDragging = false;
        let lastMouseX = 0;
        let lastMouseY = 0;
        let velYaw = 0;
        let velPitch = 0;
        let hoveredFlag = null;

        // Size setup
        let width = 500;
        let height = 500;
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

        // Spherical 3D Projection Math
        function project(lat, lon, heightOffset = 0) {
            const radLat = lat * Math.PI / 180;
            const radLon = lon * Math.PI / 180;
            const r = radius + heightOffset;

            // Rotation around Y (yaw) and X (pitch)
            const cosLat = Math.cos(radLat);
            const sinLat = Math.sin(radLat);
            const deltaLon = radLon - yaw;

            const x0 = cosLat * Math.sin(deltaLon);
            const y0 = sinLat;
            const z0 = cosLat * Math.cos(deltaLon);

            // Pitch tilt
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
                z: z, // Depth: z > 0 is front, z < 0 is back
                visible: z > -0.15
            };
        }

        // Smooth rotation to target location
        function rotateToLang(lang) {
            if (!lang) return;
            targetYaw = lang.lon * Math.PI / 180;
            targetPitch = Math.max(-0.4, Math.min(0.5, lang.lat * Math.PI / 180 * 0.45));
            isTransitioningToTarget = true;
            velYaw = 0;
            velPitch = 0;
            updateSidePanel(lang);
        }

        // Pill clicks
        pills.forEach(pill => {
            pill.addEventListener('click', () => {
                const langId = pill.getAttribute('data-lang');
                const lang = languages.find(l => l.id === langId);
                if (lang) rotateToLang(lang);
            });
        });

        // Mouse & Touch Drag Handlers
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            isTransitioningToTarget = false;
            lastMouseX = e.clientX;
            lastMouseY = e.clientY;
            velYaw = 0;
            velPitch = 0;
        });

        window.addEventListener('mouseup', () => {
            isDragging = false;
        });

        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            const mouseX = (e.clientX - rect.left) * dpr;
            const mouseY = (e.clientY - rect.top) * dpr;

            if (isDragging) {
                const dx = e.clientX - lastMouseX;
                const dy = e.clientY - lastMouseY;
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;

                velYaw = dx * 0.006;
                velPitch = dy * 0.006; // Fixed: Natural vertical drag direction

                yaw -= velYaw;
                pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
            } else {
                // Check hover on visible flags with minimum distance to prevent overlap
                let foundHover = null;
                let minDistance = Infinity;

                languages.forEach(lang => {
                    const pHeight = lang.poleHeight || 32;
                    const surface = project(lang.lat, lang.lon, 0);
                    const tip = project(lang.lat, lang.lon, pHeight);

                    if (surface.visible && surface.z > -0.1) {
                        const offX = (lang.offsetX || 0) * dpr;
                        const offY = (lang.offsetY || 0) * dpr;
                        const targetX = tip.x + offX;
                        const targetY = tip.y + offY;

                        const dist = Math.hypot(mouseX - targetX, mouseY - targetY);
                        if (dist < 32 * dpr && dist < minDistance) {
                            minDistance = dist;
                            foundHover = lang;
                        }
                    }
                });

                if (foundHover) {
                    canvas.style.cursor = 'pointer';
                    if (hoveredFlag !== foundHover) {
                        hoveredFlag = foundHover;
                        updateSidePanel(foundHover);
                    }
                } else {
                    canvas.style.cursor = isDragging ? 'grabbing' : 'grab';
                    hoveredFlag = null;
                }
            }
        });

        // Touch handlers for mobile
        canvas.addEventListener('touchstart', (e) => {
            if (e.touches.length === 1) {
                isDragging = true;
                isTransitioningToTarget = false;
                lastMouseX = e.touches[0].clientX;
                lastMouseY = e.touches[0].clientY;
                velYaw = 0;
                velPitch = 0;
            }
        }, { passive: true });

        canvas.addEventListener('touchmove', (e) => {
            if (isDragging && e.touches.length === 1) {
                const dx = e.touches[0].clientX - lastMouseX;
                const dy = e.touches[0].clientY - lastMouseY;
                lastMouseX = e.touches[0].clientX;
                lastMouseY = e.touches[0].clientY;

                velYaw = dx * 0.007;
                velPitch = dy * 0.007; // Fixed: Natural vertical drag direction

                yaw -= velYaw;
                pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
            }
        }, { passive: true });

        canvas.addEventListener('touchend', () => {
            isDragging = false;
        });

        // Theme change handler
        window.onThemeChangeForGlobe = function() {
            // Colors will adapt on next animation frame
        };

        // Render Loop (60 FPS)
        let pulseTime = 0;

        function render() {
            pulseTime += 0.04;

            // Auto-spin or smooth transition
            if (isTransitioningToTarget) {
                // Shortest angle interpolation for yaw
                let diffYaw = targetYaw - yaw;
                while (diffYaw < -Math.PI) diffYaw += Math.PI * 2;
                while (diffYaw > Math.PI) diffYaw -= Math.PI * 2;

                yaw += diffYaw * 0.08;
                pitch += (targetPitch - pitch) * 0.08;

                if (Math.abs(diffYaw) < 0.002 && Math.abs(targetPitch - pitch) < 0.002) {
                    yaw = targetYaw;
                    pitch = targetPitch;
                    isTransitioningToTarget = false;
                }
            } else if (!isDragging && !hoveredFlag) {
                // Inertia decay or slow idle rotation
                if (Math.abs(velYaw) > 0.0005) {
                    yaw -= velYaw;
                    velYaw *= 0.94;
                } else {
                    yaw -= 0.0025; // Gentle auto-rotation
                }

                if (Math.abs(velPitch) > 0.0005) {
                    pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
                    velPitch *= 0.94;
                }
            }

            // Theme detection
            const isLight = document.documentElement.getAttribute('data-theme') === 'light';
            
            // Colors (Soothing, Eye-Friendly Palette)
            const globeBgColor = isLight ? '#eef2f6' : '#0b111e';
            const graticuleColor = isLight ? 'rgba(100, 116, 139, 0.08)' : 'rgba(148, 163, 184, 0.06)';
            const ringBorder = isLight ? 'rgba(96, 165, 250, 0.25)' : 'rgba(56, 189, 248, 0.2)';
            const landFillColor = isLight ? '#cbd5e1' : '#1e293b';
            const landStrokeColor = isLight ? 'rgba(100, 116, 139, 0.35)' : 'rgba(96, 165, 250, 0.35)';

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = (width * dpr) / 2;
            const cy = (height * dpr) / 2;
            const rScaled = radius * dpr;

            // 1. Draw Base Globe Sphere (Ocean Surface)
            ctx.save();
            ctx.beginPath();
            ctx.arc(cx, cy, rScaled, 0, Math.PI * 2);
            ctx.fillStyle = globeBgColor;
            ctx.fill();

            // Soft 3D lighting depth gradient
            const innerGrad = ctx.createRadialGradient(
                cx - rScaled * 0.3, cy - rScaled * 0.3, rScaled * 0.1,
                cx, cy, rScaled
            );
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

            // Atmosphere rim line
            ctx.lineWidth = 1.2 * dpr;
            ctx.strokeStyle = ringBorder;
            ctx.stroke();
            ctx.restore();

            // 2. Draw Solid Shaded Continents (No Dots)
            if (window.WORLD_LAND_POLYGONS && window.WORLD_LAND_POLYGONS.length > 0) {
                ctx.save();
                
                // Clip strictly to globe sphere
                ctx.beginPath();
                ctx.arc(cx, cy, rScaled - 0.5 * dpr, 0, Math.PI * 2);
                ctx.clip();

                window.WORLD_LAND_POLYGONS.forEach(ring => {
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
                    ctx.fillStyle = landFillColor;
                    ctx.fill();
                    ctx.strokeStyle = landStrokeColor;
                    ctx.lineWidth = 1 * dpr;
                    ctx.stroke();
                });
                ctx.restore();
            }

            // 3. Draw Graticules (Subtle Latitude & Longitude lines over oceans)
            ctx.save();
            ctx.lineWidth = 1 * dpr;
            ctx.strokeStyle = graticuleColor;

            graticuleLines.forEach(line => {
                ctx.beginPath();
                let isDrawing = false;
                line.forEach(pt => {
                    const proj = project(pt.lat, pt.lon, 0);
                    if (proj.visible && proj.z > 0) {
                        if (!isDrawing) {
                            ctx.moveTo(proj.x, proj.y);
                            isDrawing = true;
                        } else {
                            ctx.lineTo(proj.x, proj.y);
                        }
                    } else {
                        isDrawing = false;
                    }
                });
                ctx.stroke();
            });
            ctx.restore();

            // 5. Draw Sticking-out Flags & Poles with Staggered Offsets
            const projectedFlags = languages.map(lang => {
                const pHeight = lang.poleHeight || 32;
                const surface = project(lang.lat, lang.lon, 0);
                const tip = project(lang.lat, lang.lon, pHeight);
                const offX = (lang.offsetX || 0) * dpr;
                const offY = (lang.offsetY || 0) * dpr;
                const badgeCenter = {
                    x: tip.x + offX,
                    y: tip.y + offY
                };

                return {
                    lang,
                    surface,
                    tip,
                    badgeCenter,
                    isActive: lang.id === activeLangId,
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

                // A. Base Pulse Dot on Sphere Surface
                ctx.beginPath();
                ctx.arc(surface.x, surface.y, (isActive || isHovered ? 4 : 2.8) * dpr, 0, Math.PI * 2);
                ctx.fillStyle = isLight ? '#0284c7' : '#38bdf8';
                ctx.fill();

                if (isActive || isHovered) {
                    ctx.beginPath();
                    const pulseRadius = (5.5 + Math.sin(pulseTime * 3) * 2.5) * dpr;
                    ctx.arc(surface.x, surface.y, pulseRadius, 0, Math.PI * 2);
                    ctx.strokeStyle = isLight ? 'rgba(2, 132, 199, 0.45)' : 'rgba(56, 189, 248, 0.45)';
                    ctx.lineWidth = 1.2 * dpr;
                    ctx.stroke();
                }

                // B. Sticking-out Flagpole Line
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

                // C. Flag Badge Pill at BadgeCenter
                const pillText = `${lang.flag} ${lang.name.split(' ')[0]}`;
                ctx.font = `600 ${Math.round(11 * dpr)}px sans-serif`;
                const textWidth = ctx.measureText(pillText).width;
                const padX = 8 * dpr;
                const padY = 4 * dpr;
                const pillW = textWidth + padX * 2;
                const pillH = 22 * dpr;
                const pillX = badgeCenter.x - pillW / 2;
                const pillY = badgeCenter.y - pillH / 2;
                const radiusPill = 11 * dpr;

                // Draw rounded badge rectangle
                ctx.beginPath();
                ctx.roundRect(pillX, pillY, pillW, pillH, radiusPill);

                if (isActive || isHovered) {
                    ctx.fillStyle = isLight ? '#ffffff' : '#1e293b';
                    ctx.fill();
                    ctx.strokeStyle = isLight ? '#0284c7' : '#38bdf8';
                    ctx.lineWidth = 1.8 * dpr;
                    ctx.stroke();

                    // Soft ambient glow
                    ctx.shadowColor = isLight ? 'rgba(2, 132, 199, 0.3)' : 'rgba(56, 189, 248, 0.35)';
                    ctx.shadowBlur = 8 * dpr;
                } else {
                    ctx.fillStyle = isLight ? 'rgba(255, 255, 255, 0.95)' : 'rgba(17, 24, 39, 0.9)';
                    ctx.fill();
                    ctx.strokeStyle = isLight ? 'rgba(0, 0, 0, 0.1)' : 'rgba(255, 255, 255, 0.12)';
                    ctx.lineWidth = 1 * dpr;
                    ctx.stroke();
                }

                // Text inside badge
                ctx.shadowBlur = 0;
                ctx.fillStyle = isLight ? '#0f172a' : '#f1f5f9';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(pillText, badgeCenter.x, badgeCenter.y);

                ctx.restore();
            });

            requestAnimationFrame(render);
        }

        render();
    }

    // Initialize Globe
    initGlobe();
});