import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. HTML
    html = """
<!-- Premium Booking Modal Overlay -->
<div class="booking-modal-overlay" id="bookingModal">
    <div class="booking-modal-content">
        
        <!-- Close Button -->
        <button class="close-modal-btn" id="closeModal">×</button>
        
        <div class="modal-header">
            <h2>Book Your Wash</h2>
            <p>Fill out the details below and we'll handle the rest.</p>
        </div>

        <form class="booking-form" id="laundryBookingForm">
            <!-- Row 1 -->
            <div class="form-row">
                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" placeholder="e.g. Adith" required>
                </div>
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" placeholder="+91" required>
                </div>
            </div>

            <!-- Row 2 -->
            <div class="form-row">
                <div class="form-group full-width">
                    <label>Pickup Address</label>
                    <input type="text" placeholder="House/Flat No., Street, Area" required>
                </div>
            </div>
            
            <!-- Row 3 -->
            <div class="form-row">
                <div class="form-group full-width">
                    <label>Delivery Address</label>
                    <input type="text" placeholder="Leave blank if same as pickup">
                </div>
            </div>

            <!-- Row 4 -->
            <div class="form-row">
                <div class="form-group">
                    <label>Pincode</label>
                    <input type="text" placeholder="e.g. 560076" required>
                </div>
                <div class="form-group">
                    <label>Est. Quantity (Clothes)</label>
                    <input type="number" placeholder="e.g. 15" min="1">
                </div>
            </div>

            <!-- Row 5 -->
            <div class="form-row">
                <div class="form-group full-width">
                    <label>Service Type</label>
                    <select required>
                        <option value="" disabled selected>Select a service...</option>
                        <option value="wash-fold">Wash & Fold</option>
                        <option value="wash-iron">Wash & Iron</option>
                        <option value="express">24h Express Laundry</option>
                        <option value="dry-clean">Premium Dry Cleaning</option>
                    </select>
                </div>
            </div>

            <button type="submit" class="submit-booking-btn magnetic-btn">Confirm Booking</button>
        </form>
    </div>
</div>
  <script src="script.js"></script>"""
    
    content = content.replace('  <script src="script.js"></script>', html)

    # 2. CSS
    css = """
    /* Premium Booking Modal */
    .booking-modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(15, 23, 42, 0.6); /* Dark slate glassmorphism */
        backdrop-filter: blur(8px);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        visibility: hidden;
        transition: all 0.4s ease;
    }

    .booking-modal-overlay.active {
        opacity: 1;
        visibility: visible;
    }

    .booking-modal-content {
        background: #FFFFFF;
        width: 90%;
        max-width: 550px;
        border-radius: 24px;
        padding: 40px;
        position: relative;
        box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        transform: translateY(30px) scale(0.95);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .booking-modal-overlay.active .booking-modal-content {
        transform: translateY(0) scale(1);
    }

    .close-modal-btn {
        position: absolute;
        top: 20px;
        right: 25px;
        background: none;
        border: none;
        font-size: 28px;
        color: #6B7280;
        cursor: pointer;
        transition: color 0.2s ease;
    }

    .close-modal-btn:hover {
        color: #E86A10;
    }

    .modal-header h2 {
        color: #1F2937;
        font-size: 28px;
        margin-bottom: 5px;
        font-weight: 800;
    }

    .modal-header p {
        color: #6B7280;
        font-size: 14px;
        margin-bottom: 25px;
    }

    .booking-form .form-row {
        display: flex;
        gap: 15px;
        margin-bottom: 15px;
    }

    .booking-form .form-group {
        flex: 1;
        display: flex;
        flex-direction: column;
    }

    .booking-form .full-width {
        flex: 100%;
    }

    .booking-form label {
        font-size: 12px;
        font-weight: 700;
        color: #374151;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .booking-form input, .booking-form select {
        padding: 12px 16px;
        border: 1.5px solid #E5E7EB;
        border-radius: 10px;
        font-size: 14px;
        font-family: inherit;
        outline: none;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .booking-form input:focus, .booking-form select:focus {
        border-color: #E86A10;
        box-shadow: 0 0 0 3px rgba(232, 106, 16, 0.1);
    }

    .submit-booking-btn {
        width: 100%;
        background: #10B981; /* Brand green */
        color: white;
        font-size: 16px;
        font-weight: 700;
        padding: 16px;
        border: none;
        border-radius: 12px;
        margin-top: 10px;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    .submit-booking-btn:hover {
        background: #0D9488;
    }
</style>"""
    content = content.replace('</style>', css, 1)

    # 3. JS
    js = """
// Modal Toggle Logic
const modal = document.getElementById('bookingModal');
const closeBtn = document.getElementById('closeModal');
// Select ALL "Book Now" buttons on the page
const bookNowButtons = document.querySelectorAll('.book-now-trigger'); 

// Function to open modal
function openModal(e) {
    e.preventDefault();
    modal.classList.add('active');
}

// Attach event to all book buttons
document.querySelectorAll('.book-now-trigger').forEach(btn => { 
    btn.addEventListener('click', openModal);
});

// Close when clicking the X
closeBtn.addEventListener('click', () => {
    modal.classList.remove('active');
});

// Close when clicking outside the white box
window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.classList.remove('active');
    }
});
    });
  </script>"""
    content = content.replace("    });\n  </script>", js)

    # 4. Add classes
    content = content.replace('class="mobile-link mobile-link--book magnetic-btn"', 'class="mobile-link mobile-link--book magnetic-btn book-now-trigger"')
    content = content.replace('class="btn btn--book-hero magnetic-btn"', 'class="btn btn--book-hero magnetic-btn book-now-trigger"')
    content = content.replace('class="card-action"', 'class="card-action book-now-trigger"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
