import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add CSS to the first </style> tag in the body (around line 385)
    css = """
    /* Premium Hover Lift for Cards */
    .pricing-card, .step-card, .service-card {
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
        will-change: transform;
    }

    .pricing-card:hover, .step-card:hover, .service-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 25px 50px rgba(232, 106, 16, 0.08), 0 10px 20px rgba(0, 0, 0, 0.04);
        /* If your cards have borders, this softly highlights them in brand orange */
        border-color: rgba(232, 106, 16, 0.2); 
    }
</style>"""
    
    # We will replace the first </style> we find after the body starts, or just append to the head.
    # Let's just find "</style>" globally but only replace the first occurrence that makes sense.
    content = content.replace("</style>", css, 1)

    # JS
    js = """
// Register ScrollTrigger (Make sure you have the ScrollTrigger CDN linked in your head!)
gsap.registerPlugin(ScrollTrigger);

// ----------------------------------------------------
// 1. Smooth Scroll Reveals (Fade & Slide Up)
// ----------------------------------------------------
// This targets everything with the 'reveal-up' class
gsap.utils.toArray('.reveal-up').forEach(function(card) {
    gsap.from(card, {
        scrollTrigger: {
            trigger: card,
            start: "top 85%", // Triggers when the top of the card is 85% down the screen
            toggleActions: "play none none none" // Plays once, doesn't reverse on scroll up
        },
        y: 50,
        opacity: 0,
        duration: 0.9,
        ease: "power3.out"
    });
});

// ----------------------------------------------------
// 2. Magnetic CTA Button Effect
// ----------------------------------------------------
const magneticButtons = document.querySelectorAll('.magnetic-btn');

magneticButtons.forEach(function(btn) {
    // When the mouse moves over the button, pull it towards the cursor
    btn.addEventListener('mousemove', function(e) {
        const position = btn.getBoundingClientRect();
        const x = e.clientX - position.left - position.width / 2;
        const y = e.clientY - position.top - position.height / 2;
        
        gsap.to(btn, {
            x: x * 0.3, // Adjust this multiplier to make the pull stronger or weaker
            y: y * 0.3,
            duration: 0.5,
            ease: "power2.out"
        });
    });

    // When the mouse leaves, cleanly snap it back to the center
    btn.addEventListener('mouseleave', function() {
        gsap.to(btn, {
            x: 0,
            y: 0,
            duration: 0.7,
            ease: "elastic.out(1, 0.3)" // Gives it that satisfying "boing" snap back
        });
    });
});
    });
  </script>"""

    content = content.replace("    });\n  </script>", js)

    # HTML Class Additions
    content = content.replace('class="mobile-link mobile-link--book"', 'class="mobile-link mobile-link--book magnetic-btn"')
    content = content.replace('class="btn btn--book-hero"', 'class="btn btn--book-hero magnetic-btn"')
    content = content.replace('class="service-card"', 'class="service-card reveal-up"')
    content = content.replace('class="service-card most-popular reveal-up"', 'class="service-card most-popular reveal-up"') # just in case
    content = content.replace('class="step-card"', 'class="step-card reveal-up"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
