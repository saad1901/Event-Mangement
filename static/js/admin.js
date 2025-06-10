// Admin Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeTabs();
    initializeModals();
    initializeCharts();
    setupEventListeners();
});

// Tab Navigation
function initializeTabs() {
    // Get all nav items and tabs
    const navItems = document.querySelectorAll('.nav-item');
    const tabs = document.querySelectorAll('.admin-tab');
    
    // Set first tab as active by default if no active tab
    if (!document.querySelector('.nav-item.active')) {
        navItems[0]?.classList.add('active');
        tabs[0]?.classList.add('active');
    }
    
    // Add click event listeners to nav items
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            // Get the target tab id
            const targetId = this.getAttribute('data-target');
            
            // Remove active class from all nav items and tabs
            navItems.forEach(nav => nav.classList.remove('active'));
            tabs.forEach(tab => tab.classList.remove('active'));
            
            // Add active class to clicked nav item and corresponding tab
            this.classList.add('active');
            document.getElementById(targetId)?.classList.add('active');
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
                // If edit button with data-id attribute, populate form
                if (this.hasAttribute('data-id')) {
                    const itemId = this.getAttribute('data-id');
                    populateModalForm(modalId, itemId);
                }
                
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

// Populate form fields when editing items
function populateModalForm(modalId, itemId) {
    // This function will be implemented to fetch and fill data
    // For demonstration, we'll use mock data
    console.log(`Populating ${modalId} with data for item ${itemId}`);
    
    // Example for different forms
    switch(modalId) {
        case 'eventModal':
            populateEventForm(itemId);
            break;
        case 'userModal':
            populateUserForm(itemId);
            break;
        case 'registrationModal':
            populateRegistrationForm(itemId);
            break;
    }
}

// Example functions to populate different forms
function populateEventForm(eventId) {
    // In a real app, you would fetch this data from the server
    // This is just a mockup for demonstration
    const mockEvent = {
        id: eventId,
        title: 'Example Event ' + eventId,
        description: 'This is a sample event description for testing purposes.',
        date: '2023-12-15',
        time: '18:00',
        location: 'Conference Center',
        capacity: 100,
        price: 25.99,
        status: 'upcoming'
    };
    
    // Fill the form fields
    const form = document.querySelector('#eventModal form');
    if (form) {
        form.querySelector('#event-title').value = mockEvent.title;
        form.querySelector('#event-description').value = mockEvent.description;
        form.querySelector('#event-date').value = mockEvent.date;
        form.querySelector('#event-time').value = mockEvent.time;
        form.querySelector('#event-location').value = mockEvent.location;
        form.querySelector('#event-capacity').value = mockEvent.capacity;
        form.querySelector('#event-price').value = mockEvent.price;
        form.querySelector('#event-status').value = mockEvent.status;
        
        // Update form action or set data attribute for submission
        form.setAttribute('data-edit-id', eventId);
    }
}

function populateUserForm(userId) {
    // Mock user data
    const mockUser = {
        id: userId,
        name: 'User ' + userId,
        email: 'user' + userId + '@example.com',
        phone: '555-123-456' + userId,
        role: userId % 2 === 0 ? 'admin' : 'user',
        status: 'active'
    };
    
    // Fill the form fields
    const form = document.querySelector('#userModal form');
    if (form) {
        form.querySelector('#user-name').value = mockUser.name;
        form.querySelector('#user-email').value = mockUser.email;
        form.querySelector('#user-phone').value = mockUser.phone;
        form.querySelector('#user-role').value = mockUser.role;
        form.querySelector('#user-status').value = mockUser.status;
        
        form.setAttribute('data-edit-id', userId);
    }
}

function populateRegistrationForm(registrationId) {
    // Mock registration data
    const mockRegistration = {
        id: registrationId,
        eventId: '1',
        userId: '2',
        registrationDate: '2023-11-25',
        status: 'confirmed',
        paymentStatus: 'paid',
        ticketQuantity: 2
    };
    
    // Fill the form fields
    const form = document.querySelector('#registrationModal form');
    if (form) {
        form.querySelector('#registration-event').value = mockRegistration.eventId;
        form.querySelector('#registration-user').value = mockRegistration.userId;
        form.querySelector('#registration-date').value = mockRegistration.registrationDate;
        form.querySelector('#registration-status').value = mockRegistration.status;
        form.querySelector('#registration-payment').value = mockRegistration.paymentStatus;
        form.querySelector('#registration-quantity').value = mockRegistration.ticketQuantity;
        
        form.setAttribute('data-edit-id', registrationId);
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
            event.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const formObject = {};
            formData.forEach((value, key) => {
                formObject[key] = value;
            });
            
            // Check if this is an edit (has data-edit-id)
            const editId = this.getAttribute('data-edit-id');
            
            // Log the data (would be sent to server in a real app)
            console.log('Form submitted:', 
                editId ? `Editing item ${editId}` : 'Creating new item', 
                formObject
            );
            
            // Close the modal
            const modal = this.closest('.modal');
            if (modal) closeModal(modal);
            
            // Show success message (would be based on server response)
            showNotification('Success!', 
                editId ? 'Item updated successfully.' : 'Item created successfully.', 
                'success'
            );
        });
    });
    
    // Delete buttons
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-id');
            const itemType = this.getAttribute('data-type');
            
            if (confirm(`Are you sure you want to delete this ${itemType}?`)) {
                console.log(`Deleting ${itemType} with ID ${itemId}`);
                
                // In a real app, send delete request to server
                // For demo, we'll just show a notification
                showNotification('Deleted!', `${itemType} has been deleted.`, 'success');
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
    if (typeof Chart !== 'undefined') {
        Chart.instances.forEach(instance => {
            instance.resize();
        });
    }
}); 