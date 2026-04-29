// ====================================================
// SoundSpecies — UI Scripts (Enhanced)
// ====================================================

document.addEventListener('DOMContentLoaded', function () {

    // ====== DRAG & DROP UPLOAD ======
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('audioFileInput');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    const selectedFileName = document.getElementById('selectedFileName');
    const previewContainer = document.getElementById('audioPreviewContainer');

    if (uploadArea && fileInput) {
        ['dragenter', 'dragover'].forEach(event => {
            uploadArea.addEventListener(event, function (e) {
                e.preventDefault();
                uploadArea.classList.add('drag-over');
            });
        });

        ['dragleave', 'drop'].forEach(event => {
            uploadArea.addEventListener(event, function (e) {
                e.preventDefault();
                uploadArea.classList.remove('drag-over');
            });
        });

        uploadArea.addEventListener('drop', function (e) {
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                fileInput.files = files;
                handleFileSelect(files[0]);
            }
        });

        fileInput.addEventListener('change', function () {
            if (this.files.length > 0) {
                handleFileSelect(this.files[0]);
            }
        });
    }

    function handleFileSelect(file) {
        if (fileNameDisplay && selectedFileName) {
            selectedFileName.textContent = file.name;
            fileNameDisplay.classList.add('visible');
        }

        if (previewContainer) {
            previewContainer.innerHTML = '';
            const audio = document.createElement('audio');
            audio.src = URL.createObjectURL(file);
            audio.controls = true;

            const wrapper = document.createElement('div');
            wrapper.classList.add('audio-preview-card');
            wrapper.innerHTML = '<span style="font-size: 1.1rem;">🎵</span>';
            wrapper.appendChild(audio);
            previewContainer.appendChild(wrapper);
        }
    }

    // ====== LOADING SPINNER ======
    const predictForm = document.getElementById('predictForm');
    const loadingOverlay = document.getElementById('loadingOverlay');

    if (predictForm && loadingOverlay) {
        predictForm.addEventListener('submit', function () {
            loadingOverlay.classList.add('active');
        });
    }

    // ====== ACTIVE NAV ======
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (currentPath === href || (href !== '/' && currentPath.startsWith(href))) {
            link.classList.add('active');
        } else if (href === '/' && currentPath === '/') {
            link.classList.add('active');
        }
    });

    // ====== STAGGER ANIMATIONS ======
    document.querySelectorAll('.card').forEach((card, i) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(16px)';
        setTimeout(() => {
            card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 80 + i * 60);
    });

    // ====== HAMBURGER MENU ======
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const navbarLinks = document.getElementById('navbarLinks');

    if (hamburgerBtn && navbarLinks) {
        // Create overlay
        const overlay = document.createElement('div');
        overlay.classList.add('nav-overlay');
        document.body.appendChild(overlay);

        hamburgerBtn.addEventListener('click', function () {
            hamburgerBtn.classList.toggle('active');
            navbarLinks.classList.toggle('open');
            overlay.classList.toggle('active');
        });

        overlay.addEventListener('click', function () {
            hamburgerBtn.classList.remove('active');
            navbarLinks.classList.remove('open');
            overlay.classList.remove('active');
        });

        // Close menu when a link is clicked
        navbarLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function () {
                hamburgerBtn.classList.remove('active');
                navbarLinks.classList.remove('open');
                overlay.classList.remove('active');
            });
        });
    }

    // ====== SCROLL REVEAL ======
    const revealElements = document.querySelectorAll('.scroll-reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, idx) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('revealed');
                    }, idx * 100);
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        revealElements.forEach(el => revealObserver.observe(el));
    }

    // ====== TYPEWRITER EFFECT ======
    const typewriterEl = document.getElementById('heroTypewriter');
    if (typewriterEl) {
        const text = typewriterEl.textContent;
        typewriterEl.textContent = '';
        let charIndex = 0;

        function typeChar() {
            if (charIndex < text.length) {
                typewriterEl.textContent += text.charAt(charIndex);
                charIndex++;
                setTimeout(typeChar, 90);
            }
        }

        setTimeout(typeChar, 400);
    }

});


// ====== CELEBRATION PARTICLES ======
function triggerCelebration(emoji) {
    const container = document.getElementById('particleContainer');
    if (!container) return;

    const emojis = [emoji, '✨', '🌟', '💫', emoji, '🎶', '⭐'];
    const count = 24;

    for (let i = 0; i < count; i++) {
        setTimeout(() => {
            const p = document.createElement('div');
            p.classList.add('particle');
            p.textContent = emojis[Math.floor(Math.random() * emojis.length)];
            p.style.left = Math.random() * 100 + '%';
            p.style.top = '-20px';
            p.style.animationDuration = (2.5 + Math.random() * 1.5) + 's';
            p.style.fontSize = (1 + Math.random() * 1.2) + 'rem';
            container.appendChild(p);

            setTimeout(() => p.remove(), 4000);
        }, i * 70);
    }
}


// ====== 3D CURSOR-TRACKING EMOJI ======
function initCursorTrackingEmoji() {
    const emojiContainer = document.getElementById('resultEmoji');
    if (!emojiContainer) return;

    const emojiChar = emojiContainer.querySelector('.emoji-character');
    const emojiGlow = emojiContainer.querySelector('.emoji-glow');
    if (!emojiChar) return;

    const maxRotation = 25;  // Max degrees of rotation
    const maxLift = 16;       // Max pixels of vertical lift
    let resetTimeout = null;

    // Track mouse on the entire result card
    const resultCard = emojiContainer.closest('.result-card') || document.body;

    resultCard.addEventListener('mousemove', function (e) {
        // Get emoji center position
        const rect = emojiContainer.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        // Calculate distance and angle from cursor to emoji center
        const deltaX = e.clientX - centerX;
        const deltaY = e.clientY - centerY;
        const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);

        // Only respond within a reasonable radius (400px)
        const maxDist = 400;
        const intensity = Math.max(0, 1 - distance / maxDist);

        if (intensity > 0) {
            emojiContainer.classList.add('cursor-active');

            // Calculate rotation (emoji looks toward cursor)
            const rotateY = (deltaX / maxDist) * maxRotation;
            const rotateX = -(deltaY / maxDist) * maxRotation;
            const lift = intensity * maxLift;
            const scale = 1 + intensity * 0.12;

            // Apply 3D transform
            emojiChar.style.transform = `
                translateY(-${lift}px)
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                scale(${scale})
            `;

            // Dynamic shadow based on tilt
            const shadowX = -rotateY * 0.8;
            const shadowY = 20 + rotateX * 0.5;
            const shadowBlur = 30 + intensity * 15;
            emojiChar.style.filter = `drop-shadow(${shadowX}px ${shadowY}px ${shadowBlur}px rgba(0, 0, 0, 0.4))`;

            // Move glow slightly opposite to create depth
            if (emojiGlow) {
                emojiGlow.style.transform = `translate(calc(-50% + ${-deltaX * 0.05}px), calc(-50% + ${-deltaY * 0.05}px)) scale(${1 + intensity * 0.3})`;
                emojiGlow.style.opacity = 0.6 + intensity * 0.4;
            }

            // Clear any pending reset
            if (resetTimeout) clearTimeout(resetTimeout);
        }
    });

    resultCard.addEventListener('mouseleave', function () {
        // Smoothly return to idle state
        resetTimeout = setTimeout(() => {
            emojiContainer.classList.remove('cursor-active');
            emojiChar.style.transform = '';
            emojiChar.style.filter = '';
            if (emojiGlow) {
                emojiGlow.style.transform = '';
                emojiGlow.style.opacity = '';
            }
        }, 100);
    });

    // Touch support: tilt based on touch position
    resultCard.addEventListener('touchmove', function (e) {
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousemove', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        resultCard.dispatchEvent(mouseEvent);
    }, { passive: true });

    resultCard.addEventListener('touchend', function () {
        const leaveEvent = new MouseEvent('mouseleave');
        resultCard.dispatchEvent(leaveEvent);
    });
}
