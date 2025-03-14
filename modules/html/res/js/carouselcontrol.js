document.addEventListener ('DOMContentLoaded', () => {

    $('#slider').on('slid.bs.carousel', function (event) {
        $('video').each(function () {
            this.pause();
            this.currentTime = 0;
            $('#slider').carousel("cycle");
        });

        const activeSlide = event.relatedTarget;

        const videoElement = $(activeSlide).find('video')[0];
        if (videoElement) {
            $('#slider').carousel('pause');
            // $("#slider").carousel('pause');
            console.log("slider paused");
            videoElement.play().catch(error => {
                console.log('Autoplay error: ', error);
                // $('#slider').carousel("cycle");
            });
        }
    });

    $('video').on('ended', function () {
        $('#slider').carousel("cycle");
    });
});