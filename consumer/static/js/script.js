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
            items:1
        }
    }
})

//initialise aos

AOS.init();

//update date
var yearSpan= document.querySelector("#year");
var currentYear= new Date().getFullYear();
if(currentYear == 2020){
    var yearTextNode=document.createTextNode("2020");
    yearTextNode.appendChild(yearTextNode)
}
else{
    var yearTextNode=document.createTextNode(`2020-${dateInstance.getFullYear}`);
    yearTextNode.appendChild(yearTextNode);
}