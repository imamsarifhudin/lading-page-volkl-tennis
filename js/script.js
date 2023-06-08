function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });

}

function toggleScroll() {
    var scrollButton = document.getElementById('scrollTop');
    var currentScroll = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;

    if (currentScroll > 0) {
        scrollToTop();
    }

    window.addEventListener('scroll', function () {
        var scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
        if (scrollPosition > 0) {
            scrollButton.style.opacity = 1;
        } else {
            scrollButton.style.opacity = 0;
        }
    });
}