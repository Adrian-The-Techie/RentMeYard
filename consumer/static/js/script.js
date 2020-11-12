const menuBtn=document.querySelector('.hamburger-btn')
const navBar=document.querySelector('.nav-bar')

let showMenu=false;

menuBtn.addEventListener('click', toggleMenu)

function toggleMenu(){
    if(!showMenu){
        navBar.classList.add('open')

        showMenu= true;
    }

    else{
        navBar.classList.remove('open')

        showMenu = false;
    }
}

//carousel

$('.owl-carousel').owlCarousel({
    loop:true,
    // margin:10,
    items:1,
    nav:true,
    autoplay:true,
    autoplayTimeout:5000,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

//initialise aos

AOS.init();