console.log("Dress Emporium JS Loaded");

// You can add interactive elements here later.
// For example, enhancing the custom form, image sliders, etc.

document.addEventListener('DOMContentLoaded', function() {
    // Example: Add a smooth scroll to anchor links if you add them
    // document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    //     anchor.addEventListener('click', function (e) {
    //         e.preventDefault();
    //         document.querySelector(this.getAttribute('href')).scrollIntoView({
    //             behavior: 'smooth'
    //         });
    //     });
    // });

    // Alert for any external links to indicate they might leave the site
    const externalLinks = document.querySelectorAll('a[href^="http"]');
    externalLinks.forEach(link => {
        if (link.hostname !== window.location.hostname) {
            link.setAttribute('target', '_blank'); // Open in new tab
            link.setAttribute('rel', 'noopener noreferrer'); // Security measure
            // You could add a small icon or warning
        }
    });
});