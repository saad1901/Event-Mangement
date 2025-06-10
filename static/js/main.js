// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            nav.classList.toggle('active');
            // Toggle between menu and close icon
            const icon = this.querySelector('i');
            if (icon.classList.contains('fa-bars')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (nav && nav.classList.contains('active') && !nav.contains(event.target) && !menuToggle.contains(event.target)) {
            nav.classList.remove('active');
            const icon = menuToggle.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Offset for fixed header
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (nav && nav.classList.contains('active')) {
                    nav.classList.remove('active');
                    const icon = menuToggle.querySelector('i');
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    });
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    
                    // Add error message if not exists
                    let errorMsg = field.nextElementSibling;
                    if (!errorMsg || !errorMsg.classList.contains('error-message')) {
                        errorMsg = document.createElement('div');
                        errorMsg.classList.add('error-message');
                        errorMsg.textContent = 'This field is required';
                        field.parentNode.insertBefore(errorMsg, field.nextSibling);
                    }
                } else {
                    field.classList.remove('error');
                    
                    // Remove error message if exists
                    const errorMsg = field.nextElementSibling;
                    if (errorMsg && errorMsg.classList.contains('error-message')) {
                        errorMsg.remove();
                    }
                }
                
                // Email validation
                if (field.type === 'email' && field.value) {
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(field.value)) {
                        isValid = false;
                        field.classList.add('error');
                        
                        // Add error message if not exists
                        let errorMsg = field.nextElementSibling;
                        if (!errorMsg || !errorMsg.classList.contains('error-message')) {
                            errorMsg = document.createElement('div');
                            errorMsg.classList.add('error-message');
                            errorMsg.textContent = 'Please enter a valid email address';
                            field.parentNode.insertBefore(errorMsg, field.nextSibling);
                        } else {
                            errorMsg.textContent = 'Please enter a valid email address';
                        }
                    }
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
    
    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            
            if (emailInput && emailInput.value.trim()) {
                // Show success message
                const successMsg = document.createElement('div');
                successMsg.classList.add('success-message');
                successMsg.textContent = 'Thank you for subscribing!';
                this.innerHTML = '';
                this.appendChild(successMsg);
            }
        });
    }
    
    // Animate elements on scroll
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    function checkIfInView() {
        animateElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('visible');
            }
        });
    }
    
    // Initial check
    if (animateElements.length > 0) {
        checkIfInView();
        window.addEventListener('scroll', checkIfInView);
    }
    
    // Event countdown timer
    const countdownElements = document.querySelectorAll('.countdown');
    
    function updateCountdown() {
        countdownElements.forEach(countdown => {
            const eventDate = new Date(countdown.getAttribute('data-event-date')).getTime();
            const now = new Date().getTime();
            const timeLeft = eventDate - now;
            
            if (timeLeft > 0) {
                const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
                const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
                
                countdown.innerHTML = `
                    <div class="countdown-item"><span>${days}</span> Days</div>
                    <div class="countdown-item"><span>${hours}</span> Hours</div>
                    <div class="countdown-item"><span>${minutes}</span> Minutes</div>
                    <div class="countdown-item"><span>${seconds}</span> Seconds</div>
                `;
            } else {
                countdown.innerHTML = '<div class="event-started">Event has started!</div>';
            }
        });
    }
    
    if (countdownElements.length > 0) {
        updateCountdown();
        setInterval(updateCountdown, 1000);
    }
    
    // Ticket validation
    const validateTicketForm = document.querySelector('#validate-ticket-form');
    if (validateTicketForm) {
        validateTicketForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const ticketInput = this.querySelector('input[name="ticket_code"]');
            
            if (ticketInput && ticketInput.value.trim()) {
                // Mock ticket validation (replace with actual AJAX call in production)
                const resultContainer = document.querySelector('#validation-result');
                if (resultContainer) {
                    resultContainer.innerHTML = '<div class="loading">Validating ticket...</div>';
                    
                    // Simulate API call with timeout
                    setTimeout(() => {
                        // This is just a frontend mockup - replace with actual validation logic
                        if (ticketInput.value.length === 10) {
                            resultContainer.innerHTML = '<div class="validation-success">Ticket is valid! <i class="fas fa-check-circle"></i></div>';
                        } else {
                            resultContainer.innerHTML = '<div class="validation-error">Invalid ticket code. Please try again. <i class="fas fa-times-circle"></i></div>';
                        }
                    }, 1500);
                }
            }
        });
    }
}); 