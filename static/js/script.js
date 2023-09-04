
// Inicializa el carrusel para juegos de PC
var swiperPC = new Swiper(".mySwiperPC", {
    slidesPerView: 3,
    spaceBetween: 0,
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    coverflowEffect: {
        rotate: 15,
        stretch: 0,
        depth: 300,
        modifier: 1,
        slideShadows: true,
    },
    loop: true,

    breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        480: {
          slidesPerView: 2,
          spaceBetween: 20
        },
        640: {
          slidesPerView: 3,
          spaceBetween: 30
        },
        // 768: {
        //   slidesPerView: 5,
        //   spaceBetween: 40
        // },
        // 1024: {
        //   slidesPerView: 6,
        //   spaceBetween: 50
        // },
        // 1440: {
        //   slidesPerView: 7,
        //   spaceBetween: 60
        // },
        // 2560: {
        //   slidesPerView: 8,
        //   spaceBetween: 70
        // }
      },
});

// Inicializa el carrusel para juegos de PS2
var swiperPS2 = new Swiper(".mySwiperPS2", {
    slidesPerView: 3, 
    spaceBetween: 0, 
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    coverflowEffect: {
        rotate: 15,
        stretch: 0,
        depth: 300,
        modifier: 1,
        slideShadows: true,
    },
    loop: true,
    
    breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        480: {
          slidesPerView: 2,
          spaceBetween: 20
        },
        640: {
          slidesPerView: 3,
          spaceBetween: 30
        },
        // 768: {
        //   slidesPerView: 5,
        //   spaceBetween: 40
        // },
        // 1024: {
        //   slidesPerView: 6,
        //   spaceBetween: 50
        // },
        // 1440: {
        //   slidesPerView: 7,
        //   spaceBetween: 60
        // },
        // 2560: {
        //   slidesPerView: 8,
        //   spaceBetween: 70
        // }
      },
});

