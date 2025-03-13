$(function () {

    $('#slider').on('slide.bs.carousel', function (event) {
        // $('video').each(function () {
        //     this.pause();
        //     this.currentTime = 0;
        //     $('#slider').carousel("cycle");
        // });

        const activeSlide = event.relatedTarget;

        const videoElement = $(activeSlide).find('video')[0];
        if (videoElement) {
            $('.carousel').carousel('pause')
            // $("#slider").carousel('pause');
            console.log("slider paused");
            videoElement.play().catch(error => {
                console.log('Autoplay error: ', error);
                // $('#slider').carousel("cycle");
            });
        }
    });

    // $('video').on('ended', function () {
    //     $('#slider').carousel("cycle");
    // });
});

// document.addEventListener('DOMContentLoaded', function () {
//     const carouselElement = document.getElementById('slider');
//     const videoElement = document.getElementById('carousel-video');
//     console.log("test");
//     // Pause the carousel when the video starts to play
//     carouselElement.addEventListener('slide.bs.carousel', function (event) {
//         var activeSlide = event.relatedTarget;
//         console.log(activeSlide);
//         if (activeSlide.id === 'video-slide') {
//             $('#slider').carousel('pause'); // Pause the carousel
//             videoElement.play();
//         }
//     });
//
//     // Resume the carousel when the video ends
//     videoElement.addEventListener('ended', function () {
//         $('#slider').carousel('cycle'); // Resume the carousel
//     });
//
//     // Optionally pause the carousel if play button is directly clicked
//     videoElement.addEventListener('play', function () {
//         $('#slider').carousel('pause');
//     });
// });