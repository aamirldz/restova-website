document.addEventListener('DOMContentLoaded', () => {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ═══════════════════════════════════════
    // 1. SCROLL REVEAL
    // ═══════════════════════════════════════
    if (!prefersReducedMotion) {
        const revealObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    revealObs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));
    } else {
        document.querySelectorAll('.reveal').forEach(el => el.classList.add('revealed'));
    }

    // ═══════════════════════════════════════
    // 2. NAVBAR SCROLL
    // ═══════════════════════════════════════
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        requestAnimationFrame(() => {
            if (window.scrollY > 60) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
            lastScroll = window.scrollY;
        });
    }, { passive: true });

    // ═══════════════════════════════════════
    // 3. MOBILE MENU
    // ═══════════════════════════════════════
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            mobileMenu.classList.toggle('active');
        });
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
            });
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
                menuToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
            }
        });
    }

    // ═══════════════════════════════════════
    // 4. PRODUCT TABS
    // ═══════════════════════════════════════
    document.querySelectorAll('.product-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.dataset.tab;
            document.querySelectorAll('.product-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.product-panel').forEach(p => p.classList.remove('active'));
            tab.classList.add('active');
            const panel = document.querySelector(`.product-panel[data-panel="${target}"]`);
            if (panel) panel.classList.add('active');
        });
    });

    // ═══════════════════════════════════════
    // 5. WORKFLOW SCROLL ANIMATION
    // ═══════════════════════════════════════
    const workflowSection = document.getElementById('workflow');
    const workflowFill = document.getElementById('workflowFill');
    const workflowSteps = document.querySelectorAll('.workflow-step');

    if (workflowSection && workflowFill && !prefersReducedMotion) {
        window.addEventListener('scroll', () => {
            requestAnimationFrame(() => {
                const rect = workflowSection.getBoundingClientRect();
                const vh = window.innerHeight;
                let progress = (vh - rect.top) / (rect.height + vh * 0.5);
                progress = Math.max(0, Math.min(1, progress));
                workflowFill.style.height = `${progress * 100}%`;
                const step = 1 / workflowSteps.length;
                workflowSteps.forEach((s, i) => {
                    if (progress > i * step + step * 0.15) {
                        s.classList.add('active');
                    } else {
                        s.classList.remove('active');
                    }
                });
            });
        }, { passive: true });
    } else {
        workflowSteps.forEach(s => s.classList.add('active'));
    }

    // ═══════════════════════════════════════
    // 6. REAL-TIME SYNC DEMO
    // ═══════════════════════════════════════
    const realtimeSection = document.getElementById('realtime');
    let syncInterval = null;

    if (realtimeSection && !prefersReducedMotion) {
        const syncCaptain = document.getElementById('syncCaptain');
        const syncPOS = document.getElementById('syncPOS');
        const syncKDS = document.getElementById('syncKDS');
        const syncItem1 = document.getElementById('syncItem1');
        const syncTableStatus = document.getElementById('syncTableStatus');
        const syncCartPreview = document.getElementById('syncCartPreview');
        const syncKot = document.getElementById('syncKot');
        const syncPulse1 = document.getElementById('syncPulse1');
        const syncPulse2 = document.getElementById('syncPulse2');
        const syncPulse3 = document.getElementById('syncPulse3');

        function resetSync() {
            [syncCaptain, syncPOS, syncKDS].forEach(d => d && d.classList.remove('active'));
            [syncPulse1, syncPulse2, syncPulse3].forEach(p => p && p.classList.remove('active'));
            if (syncItem1) syncItem1.classList.remove('highlight');
            if (syncTableStatus) { syncTableStatus.textContent = 'Available'; syncTableStatus.className = 'sync-status available'; }
            if (syncCartPreview) syncCartPreview.textContent = '—';
            if (syncKot) { syncKot.textContent = 'Waiting for orders...'; syncKot.classList.remove('active'); }
        }

        function runSyncDemo() {
            resetSync();
            // Step 1: Captain adds item
            setTimeout(() => {
                if (syncCaptain) syncCaptain.classList.add('active');
                if (syncPulse1) syncPulse1.classList.add('active');
                if (syncItem1) syncItem1.classList.add('highlight');
            }, 500);
            // Step 2: POS updates
            setTimeout(() => {
                if (syncCaptain) syncCaptain.classList.remove('active');
                if (syncPulse1) syncPulse1.classList.remove('active');
                if (syncPOS) syncPOS.classList.add('active');
                if (syncPulse2) syncPulse2.classList.add('active');
                if (syncTableStatus) { syncTableStatus.textContent = 'Occupied'; syncTableStatus.className = 'sync-status occupied'; }
                if (syncCartPreview) syncCartPreview.textContent = 'Butter Chicken ×1  ₹450';
            }, 2000);
            // Step 3: KDS receives KOT
            setTimeout(() => {
                if (syncPOS) syncPOS.classList.remove('active');
                if (syncPulse2) syncPulse2.classList.remove('active');
                if (syncKDS) syncKDS.classList.add('active');
                if (syncPulse3) syncPulse3.classList.add('active');
                if (syncKot) { syncKot.innerHTML = '<strong>KOT #15</strong> — Table 2<br>1× Butter Chicken'; syncKot.classList.add('active'); }
            }, 3500);
            // Step 4: Reset
            setTimeout(() => {
                resetSync();
            }, 6000);
        }

        const syncObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !syncInterval) {
                    runSyncDemo();
                    syncInterval = setInterval(runSyncDemo, 7000);
                } else if (!entry.isIntersecting && syncInterval) {
                    clearInterval(syncInterval);
                    syncInterval = null;
                    resetSync();
                }
            });
        }, { threshold: 0.3 });
        syncObs.observe(realtimeSection);
    }

    // ═══════════════════════════════════════
    // 7. OFFLINE DEMO
    // ═══════════════════════════════════════
    const offlineSection = document.getElementById('offline');
    let offlineInterval = null;

    if (offlineSection && !prefersReducedMotion) {
        const offlineSteps = offlineSection.querySelectorAll('.offline-step');
        let currentStep = 0;

        function runOfflineDemo() {
            offlineSteps.forEach(s => s.classList.remove('active'));
            offlineSteps[currentStep].classList.add('active');
            currentStep = (currentStep + 1) % offlineSteps.length;
        }

        const offlineObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !offlineInterval) {
                    currentStep = 0;
                    runOfflineDemo();
                    offlineInterval = setInterval(runOfflineDemo, 2000);
                } else if (!entry.isIntersecting && offlineInterval) {
                    clearInterval(offlineInterval);
                    offlineInterval = null;
                }
            });
        }, { threshold: 0.3 });
        offlineObs.observe(offlineSection);
    }

    // ═══════════════════════════════════════
    // 8. HERO ANIMATION
    // ═══════════════════════════════════════
    if (!prefersReducedMotion) {
        let heroInterval = null;
        function runHeroAnimation() {
            const captainSend = document.getElementById('heroCaptainSend');
            const cartItem = document.getElementById('heroCartItem');
            const kotCard = document.getElementById('heroKotCard');
            const captainItem = document.getElementById('heroCaptainItem');
            const t2 = document.getElementById('heroT2');

            // Reset
            if (captainSend) captainSend.style.transform = '';
            if (cartItem) cartItem.classList.remove('highlight');
            if (kotCard) kotCard.classList.remove('highlight');
            if (captainItem) captainItem.classList.remove('highlight');

            // Step 1: Captain highlights order
            setTimeout(() => { if (captainItem) captainItem.classList.add('highlight'); }, 500);
            // Step 2: Send button pulses
            setTimeout(() => { if (captainSend) captainSend.style.transform = 'scale(0.95)'; }, 1200);
            setTimeout(() => { if (captainSend) captainSend.style.transform = ''; }, 1400);
            // Step 3: POS cart highlights
            setTimeout(() => {
                if (captainItem) captainItem.classList.remove('highlight');
                if (cartItem) cartItem.classList.add('highlight');
            }, 2000);
            // Step 4: KDS card highlights
            setTimeout(() => {
                if (cartItem) cartItem.classList.remove('highlight');
                if (kotCard) kotCard.classList.add('highlight');
            }, 3200);
            // Step 5: Reset
            setTimeout(() => {
                if (kotCard) kotCard.classList.remove('highlight');
            }, 5000);
        }

        // Only run hero animation when visible
        const heroObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !heroInterval) {
                    runHeroAnimation();
                    heroInterval = setInterval(runHeroAnimation, 6000);
                } else if (!entry.isIntersecting && heroInterval) {
                    clearInterval(heroInterval);
                    heroInterval = null;
                }
            });
        }, { threshold: 0.2 });
        const heroEl = document.getElementById('hero');
        if (heroEl) heroObs.observe(heroEl);
    }

    // ═══════════════════════════════════════
    // 9. FAQ ACCORDION
    // ═══════════════════════════════════════
    document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.parentElement;
            const answer = item.querySelector('.faq-answer');
            const isOpen = item.classList.contains('active');

            // Close all others
            document.querySelectorAll('.faq-item.active').forEach(open => {
                open.classList.remove('active');
                open.querySelector('.faq-answer').style.maxHeight = '0';
            });

            if (!isOpen) {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });

    // ═══════════════════════════════════════
    // 10. REGISTRATION FORM
    // ═══════════════════════════════════════
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = document.getElementById('registerBtn');
            const name = document.getElementById('regName').value.trim();
            const owner = document.getElementById('regOwner').value.trim();
            const phone = document.getElementById('regPhone').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const city = document.getElementById('regCity').value.trim();
            const tables = document.getElementById('regTables').value || '—';
            const currentPOS = document.getElementById('regCurrentPOS').value || '—';
            const message = document.getElementById('regMessage').value.trim() || '—';

            // Validation
            if (!name || !owner || !phone || !email || !city) {
                btn.textContent = '❌ Please fill all required fields';
                btn.style.background = '#dc2626';
                setTimeout(() => { btn.textContent = 'Register via WhatsApp'; btn.style.background = ''; }, 2500);
                return;
            }
            if (phone.replace(/\D/g, '').length < 10) {
                btn.textContent = '❌ Enter a valid phone number';
                btn.style.background = '#dc2626';
                setTimeout(() => { btn.textContent = 'Register via WhatsApp'; btn.style.background = ''; }, 2500);
                return;
            }
            if (!email.includes('@') || !email.includes('.')) {
                btn.textContent = '❌ Enter a valid email';
                btn.style.background = '#dc2626';
                setTimeout(() => { btn.textContent = 'Register via WhatsApp'; btn.style.background = ''; }, 2500);
                return;
            }

            // Loading state
            btn.textContent = 'Opening WhatsApp...';
            btn.disabled = true;

            const msg = `🏪 *New Restaurant Registration — Restova*

*Restaurant:* ${name}
*Owner:* ${owner}
*Phone:* ${phone}
*Email:* ${email}
*City:* ${city}
*Tables:* ${tables}
*Current POS:* ${currentPOS}
*Message:* ${message}`;

            const waUrl = `https://wa.me/919939525676?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank');

            // Show success
            setTimeout(() => {
                const formSuccess = document.getElementById('formSuccess');
                registerForm.querySelectorAll('.form-row, .form-group, .btn-primary, .form-note').forEach(el => el.style.display = 'none');
                if (formSuccess) formSuccess.style.display = 'block';
            }, 500);
        });
    }

    // ═══════════════════════════════════════
    // 11. SMOOTH SCROLL
    // ═══════════════════════════════════════
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const id = this.getAttribute('href');
            if (id === '#') return;
            const target = document.querySelector(id);
            if (target) {
                e.preventDefault();
                const offset = 80;
                const pos = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top: pos, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
            }
        });
    });
});

// Workflow interactions — scoped per container


function switchWorkflow(stepEl, auto = false) {
    if (!stepEl) return;

    // Scope to the parent .workflow-container only
    const container = stepEl.closest('.workflow-container');
    if (!container) return;

    // Clear active states on steps WITHIN THIS CONTAINER ONLY
    container.querySelectorAll('.w-step').forEach(s => {
        s.classList.remove('active');
        const bar = s.querySelector('.w-step-progress-bar');
        if (bar) { bar.style.transition = 'none'; bar.style.width = '0%'; }
    });

    // Set clicked step as active
    stepEl.classList.add('active');

    // Clear active state on images WITHIN THIS CONTAINER ONLY
    container.querySelectorAll('.workflow-visual img').forEach(img => img.classList.remove('active'));

    // Show target image
    const targetId = stepEl.getAttribute('data-img');
    const targetImg = document.getElementById(targetId);
    if (targetImg) targetImg.classList.add('active');

    // Morph captain phone to desktop if cpt-4 is selected
    const captainDevice = document.getElementById('captainDevice');
    if (captainDevice) {
        if (targetId === 'cpt-4') {
            captainDevice.classList.add('morph-to-desktop');
        } else if (targetId === 'cpt-1' || targetId === 'cpt-2' || targetId === 'cpt-3') {
            captainDevice.classList.remove('morph-to-desktop');
        }
    }

    // Reset and start animation for progress bar
    if (auto !== 'stop') {
        startWorkflowAutoPlay(stepEl);
    } else {
        const container = stepEl.closest(".workflow-container"); if(container.workflowInterval) clearInterval(container.workflowInterval);
    }
}

function startWorkflowAutoPlay(currentStep) {
    const container = currentStep.closest(".workflow-container"); 
    if(container && container.workflowInterval) clearInterval(container.workflowInterval);
    
    const bar = currentStep.querySelector('.w-step-progress-bar');
    if (!bar) return;

    void bar.offsetWidth;
    bar.style.transition = 'width 4s linear';
    bar.style.width = '100%';

    container.workflowInterval = setInterval(() => {
        const stepsContainer = currentStep.parentElement;
        let nextStep = currentStep.nextElementSibling;
        if (!nextStep || !nextStep.classList.contains('w-step')) {
            nextStep = stepsContainer.querySelector('.w-step');
        }
        switchWorkflow(nextStep);
    }, 4000);
}

// On page load: auto-play POS workflow
document.addEventListener('DOMContentLoaded', () => {
    const posPanel = document.querySelector('[data-panel="pos"]');
    if (posPanel && posPanel.classList.contains('active')) {
        const firstStep = posPanel.querySelector('.w-step');
        if (firstStep) startWorkflowAutoPlay(firstStep);
    }
    const ownerSection = document.getElementById('owner');
    if (ownerSection) {
        const ownerFirstStep = ownerSection.querySelector('.w-step');
        if (ownerFirstStep) startWorkflowAutoPlay(ownerFirstStep);
    }

    // Create lightbox DOM once
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.innerHTML = '<span class="lightbox-close">&times;</span><img src="" id="lightbox-img">';
    document.body.appendChild(lightbox);

    // Lightbox: click any workflow-visual to expand
    document.querySelectorAll('.workflow-visual').forEach(vis => {
        vis.addEventListener('click', () => {
            const activeImg = vis.querySelector('img.active');
            if (activeImg) {
                document.getElementById('lightbox-img').src = activeImg.src;
                lightbox.classList.add('active');
                const container = stepEl.closest(".workflow-container"); if(container.workflowInterval) clearInterval(container.workflowInterval);
            }
        });
    });

    lightbox.addEventListener('click', () => lightbox.classList.remove('active'));
});

// Tab switching: start autoplay for the selected tab's workflow
document.querySelectorAll('.product-tab').forEach(btn => {
    btn.addEventListener('click', () => {
        const container = stepEl.closest(".workflow-container"); if(container.workflowInterval) clearInterval(container.workflowInterval);
        const target = btn.getAttribute('data-tab');
        setTimeout(() => {
            const panel = document.querySelector(`.product-panel[data-panel="${target}"]`);
            if (panel) {
                const firstStep = panel.querySelector('.w-step');
                if (firstStep) switchWorkflow(firstStep);
            }
        }, 150);
    });
});

// Manual click on a step stops autoplay
document.querySelectorAll('.w-step').forEach(step => {
    step.addEventListener('click', function(e) {
        if (e.isTrusted) switchWorkflow(this, 'stop');
    });
});

// ═══════════════════════════════════════
// OWNER CAROUSEL LOGIC
// ═══════════════════════════════════════
function scrollOwnerCarousel(direction) {
    const carousel = document.getElementById('ownerCarousel');
    if (!carousel) return;
    
    // Calculate the width of one slide + gap
    const slideWidth = carousel.querySelector('.owner-slide').offsetWidth + 30; 
    
    carousel.scrollBy({
        left: direction * slideWidth,
        behavior: 'smooth'
    });
}

// ═══════════════════════════════════════
// ADVANCED OWNER DESKTOP LOGIC
// ═══════════════════════════════════════
let ownerAutoInterval;

function startOwnerAutoplay(stepNum) {
    if (ownerAutoInterval) clearInterval(ownerAutoInterval);

    const controls = document.getElementById('ownerControls');
    if (!controls) return;
    const steps = controls.querySelectorAll('.o-step');
    
    // Target the specific step's progress bar
    const currentStepEl = steps[stepNum - 1];
    if (currentStepEl) {
        const bar = currentStepEl.querySelector('.o-bar');
        if (bar) {
            void bar.offsetWidth; // trigger reflow
            bar.style.transition = 'width 4s linear';
            bar.style.width = '100%';
        }
    }

    ownerAutoInterval = setInterval(() => {
        let nextStep = stepNum + 1;
        if (nextStep > 4) nextStep = 1;
        switchOwnerStep(nextStep, true);
    }, 4000);
}

function switchOwnerStep(stepNum, auto = false) {
    const controls = document.getElementById('ownerControls');
    if (!controls) return;

    // Reset all steps
    controls.querySelectorAll('.o-step').forEach(step => {
        step.classList.remove('active');
        const bar = step.querySelector('.o-bar');
        if (bar) {
            bar.style.transition = 'none';
            bar.style.width = '0%';
        }
    });

    // Reset all images
    document.querySelectorAll('.monitor-screen img').forEach(img => {
        img.classList.remove('active');
    });

    // Set new active
    const targetImg = document.getElementById('o-img-' + stepNum);
    if (targetImg) targetImg.classList.add('active');

    // Morph captain phone to desktop if cpt-4 is selected
    const captainDevice = document.getElementById('captainDevice');
    if (captainDevice) {
        if (targetId === 'cpt-4') {
            captainDevice.classList.add('morph-to-desktop');
        } else if (targetId === 'cpt-1' || targetId === 'cpt-2' || targetId === 'cpt-3') {
            captainDevice.classList.remove('morph-to-desktop');
        }
    }

    const steps = controls.querySelectorAll('.o-step');
    if (steps[stepNum - 1]) {
        steps[stepNum - 1].classList.add('active');
    }

    if (!auto) {
        if (ownerAutoInterval) clearInterval(ownerAutoInterval);
    } else {
        startOwnerAutoplay(stepNum);
    }
}

// Start owner autoplay on load
document.addEventListener('DOMContentLoaded', () => {
    const ownerSection = document.getElementById('owner');
    if (ownerSection) {
        startOwnerAutoplay(1);
    }

    // Add Mobile Workflow Navigation Arrows dynamically
    document.querySelectorAll('.workflow-steps').forEach(stepsContainer => {
        const navDiv = document.createElement('div');
        navDiv.className = 'workflow-mobile-nav';
        navDiv.innerHTML = `
            <button class="w-nav-btn prev">❮</button>
            <button class="w-nav-btn next">❯</button>
        `;
        stepsContainer.appendChild(navDiv);

        const prevBtn = navDiv.querySelector('.prev');
        const nextBtn = navDiv.querySelector('.next');

        prevBtn.addEventListener('click', () => {
            const currentStep = stepsContainer.querySelector('.w-step.active');
            if(!currentStep) return;
            let prevStep = currentStep.previousElementSibling;
            if (!prevStep || !prevStep.classList.contains('w-step')) {
                const allSteps = stepsContainer.querySelectorAll('.w-step');
                prevStep = allSteps[allSteps.length - 1];
            }
            switchWorkflow(prevStep, 'stop');
        });

        nextBtn.addEventListener('click', () => {
            const currentStep = stepsContainer.querySelector('.w-step.active');
            if(!currentStep) return;
            let nextStep = currentStep.nextElementSibling;
            if (!nextStep || !nextStep.classList.contains('w-step')) {
                nextStep = stepsContainer.querySelector('.w-step');
            }
            switchWorkflow(nextStep, 'stop');
        });
    });
});
