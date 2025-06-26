// Admin Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeTabs();
    initializeModals();
    initializeCharts();
    setupEventListeners();
});

// Tab Navigation
// Function to initialize tabs
function initializeTabs() {
    const navItems = document.querySelectorAll('.nav-item');
    
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all items
            navItems.forEach(nav => nav.classList.remove('active'));
            
            // Add active class to clicked item
            this.classList.add('active');
        });
    });
}

// Modal Management
function initializeModals() {
    // Get all modal triggers and close buttons
    const modalTriggers = document.querySelectorAll('[data-modal-target]');
    const closeButtons = document.querySelectorAll('.close-modal');
    
    // Open modal when trigger is clicked
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal-target');
            const modal = document.getElementById(modalId);
            
            if (modal) {
                modal.style.display = 'block';
                document.body.style.overflow = 'hidden'; // Prevent scrolling
            }
        });
    });
    
    // Close modal when close button is clicked
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.modal');
            closeModal(modal);
        });
    });
    
    // Close modal when clicking outside of modal content
    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            closeModal(event.target);
        }
    });
}

// Close modal and reset form
function closeModal(modal) {
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = ''; // Restore scrolling
        
        // Reset form if exists
        const form = modal.querySelector('form');
        if (form) form.reset();
    }
}

// Initialize Chart.js charts
function initializeCharts() {
    // Ensure Chart.js is loaded
    if (typeof Chart === 'undefined') {
        console.warn('Chart.js not loaded');
        return;
    }
    
    // Event Statistics Chart
    const eventStatisticsChart = document.getElementById('eventStatisticsChart');
    if (eventStatisticsChart) {
        new Chart(eventStatisticsChart, {
            type: 'bar',
            data: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June'],
                datasets: [{
                    label: 'Event Registrations',
                    data: [65, 59, 80, 81, 56, 90],
                    backgroundColor: 'rgba(121, 40, 202, 0.6)',
                    borderColor: 'rgba(121, 40, 202, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
    
    // Revenue Chart
    const revenueChart = document.getElementById('revenueChart');
    if (revenueChart) {
        new Chart(revenueChart, {
            type: 'line',
            data: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June'],
                datasets: [{
                    label: 'Revenue ($)',
                    data: [1200, 1900, 2300, 1800, 2500, 3000],
                    fill: true,
                    backgroundColor: 'rgba(0, 212, 255, 0.2)',
                    borderColor: 'rgba(0, 212, 255, 1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
    
    // User Distribution Chart
    const userDistributionChart = document.getElementById('userDistributionChart');
    if (userDistributionChart) {
        new Chart(userDistributionChart, {
            type: 'doughnut',
            data: {
                labels: ['Regular Users', 'Premium Users', 'Administrators'],
                datasets: [{
                    data: [65, 25, 10],
                    backgroundColor: [
                        'rgba(0, 212, 255, 0.6)',
                        'rgba(121, 40, 202, 0.6)',
                        'rgba(255, 193, 7, 0.6)'
                    ],
                    borderColor: [
                        'rgba(0, 212, 255, 1)',
                        'rgba(121, 40, 202, 1)',
                        'rgba(255, 193, 7, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }
}

// Setup other event listeners
function setupEventListeners() {
    // Form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            // Do NOT prevent default, so form submits to backend
            // Optionally close modal after submission (will only work for AJAX, not normal submit)
            // const modal = this.closest('.modal');
            // if (modal) closeModal(modal);
            // Optionally show notification after backend response, not here
        });
    });
    
    // Delete buttons
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const itemId = this.getAttribute('data-id');
            const itemType = this.getAttribute('data-type');
            if (confirm(`Are you sure you want to delete this ${itemType}?`)) {
                // Create a form and submit POST to /delete_registration/<id>/
                const form = document.createElement('form');
                form.method = 'POST';
                form.action = `/superadmin/dashboard/deleteregistration/${itemId}/`;
                // Add CSRF token
                const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]');
                if (csrfToken) {
                    const csrfInput = document.createElement('input');
                    csrfInput.type = 'hidden';
                    csrfInput.name = 'csrfmiddlewaretoken';
                    csrfInput.value = csrfToken.value;
                    form.appendChild(csrfInput);
                }
                document.body.appendChild(form);
                form.submit();
            }
        });
    });
    
    // Search functionality
    const searchBoxes = document.querySelectorAll('.search-box');
    searchBoxes.forEach(box => {
        const input = box.querySelector('input');
        const button = box.querySelector('button');
        
        if (input && button) {
            button.addEventListener('click', function() {
                performSearch(input.value, this.getAttribute('data-target'));
            });
            
            input.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    performSearch(this.value, button.getAttribute('data-target'));
                }
            });
        }
    });
    
    // Filter change events
    const filterSelects = document.querySelectorAll('.filter-options select');
    filterSelects.forEach(select => {
        select.addEventListener('change', function() {
            applyFilter(this.value, this.getAttribute('data-filter-type'));
        });
    });
    
    // Registration view/edit button listeners
    // Use event delegation for dynamic rows
    const tableBody = document.querySelector('.admin-table tbody');
    if (tableBody) {
        tableBody.addEventListener('click', function(e) {
            const btn = e.target.closest('.view-btn, .edit-btn');
            if (!btn) return;
            const row = btn.closest('.registration-row');
            if (!row) return;
            // Gather data from row attributes
            const data = {
                event: row.dataset.event,
                full_name: row.dataset.full_name,
                email: row.dataset.email,
                phone: row.dataset.phone,
                wp: row.dataset.wp,
                age: row.dataset.age,
                gender: row.dataset.gender,
                date: row.dataset.date,
                status: row.dataset.status,
                ticket_count: row.dataset.ticket_count,
                payment_status: row.dataset.payment_status,
                payment_reference: row.dataset.payment_reference,
                notes: row.dataset.notes,
                special_requirements: row.dataset.special_requirements,
                payment_screenshot: row.dataset.payment_screenshot
            };
            if (btn.classList.contains('view-btn')) {
                openRegistrationModal('view', data);
            } else if (btn.classList.contains('edit-btn')) {
                // Set the form action URL dynamically
                const form = document.getElementById('edit-registration-form');
                if (form && row.dataset.id) {
                    // Use path param, not query param, to match Django URL
                    form.action = '/superadmin/dashboard/editregistration/' + row.dataset.id + '/';
                }
                openRegistrationModal('edit', data);
            }
        });
    }
}

// Registration View/Edit Modal Logic
function openRegistrationModal(mode, data) {
    if (mode === 'view') {
        const modal = document.getElementById('view-registration-modal');
        document.getElementById('view_registration_event').value = data.event || '';
        document.getElementById('view_registration_full_name').value = data.full_name || '';
        document.getElementById('view_registration_email').value = data.email || '';
        document.getElementById('view_registration_phone').value = data.phone || '';
        document.getElementById('view_registration_wp').value = data.wp || '';
        document.getElementById('view_registration_age').value = data.age || '';
        document.getElementById('view_registration_gender').value = data.gender || '';
        document.getElementById('view_registration_date').value = data.date || '';
        document.getElementById('view_registration_status').value = data.status || '';
        document.getElementById('view_registration_ticket_count').value = data.ticket_count || '';
        document.getElementById('view_registration_payment_status').value = data.payment_status || '';
        document.getElementById('view_registration_payment_reference').value = data.payment_reference || '';
        document.getElementById('view_registration_notes').value = data.notes || '';
        document.getElementById('view_registration_special_requirements').value = data.special_requirements || '';
        document.getElementById('view_registration_payment_screenshot').src = data.payment_screenshot || '';
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    } else if (mode === 'edit') {
        const modal = document.getElementById('edit-registration-modal');
        // Event select (populate with real events from Django context)
        const eventSelect = document.getElementById('edit_registration_event');
        if (eventSelect) {
            // Always clear and repopulate options
            eventSelect.innerHTML = '<option value="">Select event</option>';
            if (window.EVENT_OPTIONS && Array.isArray(window.EVENT_OPTIONS)) {
                window.EVENT_OPTIONS.forEach(ev => {
                    const opt = document.createElement('option');
                    opt.value = String(ev.id);
                    opt.textContent = ev.title;
                    eventSelect.appendChild(opt);
                });
            }
            // Set value to the event id (not title!)
            let eventId = data.event_id || '';
            if (!eventId && data.event && window.EVENT_OPTIONS) {
                // Try to find event id by title (case-insensitive)
                const found = window.EVENT_OPTIONS.find(ev => ev.title.trim().toLowerCase() === (data.event || '').trim().toLowerCase());
                if (found) eventId = String(found.id);
            }
            eventSelect.value = eventId;
        }
        // Gender select
        const genderSelect = document.getElementById('edit_registration_gender');
        if (genderSelect) {
            genderSelect.innerHTML = `
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
            `;
            genderSelect.value = (data.gender || '').toLowerCase();
        }
        // Status select
        const statusSelect = document.getElementById('edit_registration_status');
        if (statusSelect) {
            statusSelect.innerHTML = `
                <option value="registered">Registered</option>
                <option value="confirmed">Confirmed</option>
                <option value="checked_in">Checked In</option>
                <option value="eliminated">Eliminated</option>
                <option value="winner">Winner</option>
                <option value="disqualified">Disqualified</option>
                <option value="rejected">Rejected</option>
            `;
            statusSelect.value = (data.status || '').toLowerCase();
        }
        // Payment status select
        const paymentStatusSelect = document.getElementById('edit_registration_payment_status');
        if (paymentStatusSelect) {
            paymentStatusSelect.innerHTML = `
                <option value="pending">Pending</option>
                <option value="completed">Completed</option>
                <option value="failed">Failed</option>
                <option value="refunded">Refunded</option>
            `;
            let paymentStatus = (data.payment_status || '').trim().toLowerCase();
            let foundPaymentStatus = '';
            Array.from(paymentStatusSelect.options).forEach(opt => {
                const optValue = opt.value.trim().toLowerCase();
                const optText = opt.textContent.trim().toLowerCase();
                if (optValue === paymentStatus || optText === paymentStatus) {
                    foundPaymentStatus = opt.value;
                }
            });
            if (!foundPaymentStatus && paymentStatus) {
                Array.from(paymentStatusSelect.options).forEach(opt => {
                    const optValue = opt.value.trim().toLowerCase();
                    const optText = opt.textContent.trim().toLowerCase();
                    if (optValue.includes(paymentStatus) || optText.includes(paymentStatus) || paymentStatus.includes(optValue)) {
                        foundPaymentStatus = opt.value;
                    }
                });
            }
            paymentStatusSelect.value = foundPaymentStatus || '';
        }
        document.getElementById('edit_registration_full_name').value = data.full_name || '';
        document.getElementById('edit_registration_email').value = data.email || '';
        document.getElementById('edit_registration_phone').value = data.phone || '';
        document.getElementById('edit_registration_wp').value = data.wp || '';
        document.getElementById('edit_registration_age').value = data.age || '';
        document.getElementById('edit_registration_date').value = data.date || '';
        document.getElementById('edit_registration_ticket_count').value = data.ticket_count || '';
        document.getElementById('edit_registration_payment_reference').value = data.payment_reference || '';
        document.getElementById('edit_registration_notes').value = data.notes || '';
        document.getElementById('edit_registration_special_requirements').value = data.special_requirements || '';
        // Payment screenshot is file input, can't set value for security reasons
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

// Search function
function performSearch(query, targetTable) {
    console.log(`Searching for "${query}" in ${targetTable}`);
    
    // In a real app, this would filter the table or send a request to the server
    // For demo, we'll just show a notification
    showNotification('Search', `Searching for "${query}"`, 'info');
}

// Filter function
function applyFilter(value, filterType) {
    console.log(`Applying ${filterType} filter: ${value}`);
    
    // In a real app, this would filter the table or send a request to the server
    // For demo, we'll just show a notification
    showNotification('Filter Applied', `${filterType}: ${value}`, 'info');
}

// Notification system
function showNotification(title, message, type = 'info') {
    // Check if notification container exists, if not create it
    let notifContainer = document.getElementById('notification-container');
    if (!notifContainer) {
        notifContainer = document.createElement('div');
        notifContainer.id = 'notification-container';
        notifContainer.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
        `;
        document.body.appendChild(notifContainer);
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.style.cssText = `
        background-color: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#17a2b8'};
        color: white;
        padding: 15px 20px;
        margin-bottom: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        min-width: 300px;
        max-width: 400px;
        opacity: 0;
        transform: translateX(50px);
        transition: opacity 0.3s, transform 0.3s;
    `;
    
    // Add notification content
    const content = document.createElement('div');
    const titleElem = document.createElement('h4');
    titleElem.textContent = title;
    titleElem.style.margin = '0 0 5px 0';
    
    const messageElem = document.createElement('p');
    messageElem.textContent = message;
    messageElem.style.margin = '0';
    
    content.appendChild(titleElem);
    content.appendChild(messageElem);
    
    // Add close button
    const closeBtn = document.createElement('button');
    closeBtn.innerHTML = '&times;';
    closeBtn.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
        padding: 0 0 0 10px;
    `;
    
    notification.appendChild(content);
    notification.appendChild(closeBtn);
    
    // Add to container
    notifContainer.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 10);
    
    // Setup auto close
    const timeout = setTimeout(() => {
        closeNotification(notification);
    }, 5000);
    
    // Setup close button
    closeBtn.addEventListener('click', () => {
        clearTimeout(timeout);
        closeNotification(notification);
    });
}

function closeNotification(notification) {
    notification.style.opacity = '0';
    notification.style.transform = 'translateX(50px)';
    
    setTimeout(() => {
        notification.remove();
    }, 300);
}

// Data export function
function exportData(dataType) {
    console.log(`Exporting ${dataType} data`);
    
    // In a real app, this would generate and download the data
    // For demo, we'll just show a notification
    showNotification('Export Started', `${dataType} data export has begun. The file will download shortly.`, 'info');
    
    // Simulate download after a short delay
    setTimeout(() => {
        showNotification('Export Complete', `${dataType} data has been exported successfully.`, 'success');
    }, 2000);
}

// Date utilities
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

function getCurrentDate() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// Responsive adjustments
window.addEventListener('resize', function() {
    // Adjust charts if they exist
    if (typeof Chart !== 'undefined' && Chart.instances) {
        Chart.instances.forEach(instance => {
            instance.resize();
        });
    }
});