$('.owl-carousel').owlCarousel({
    loop:true,
    margin:15,
    nav:false,
    responsive:{
        0:{
            items:2
        },
        600:{
            items:3
        },
        1000:{
            items:6
        }
    }
})

// cor da página

var dark = document.getElementById('btnDark');
var light = document.getElementById('btnLight');
var body = document.querySelector('body');
dark.onclick = function(){
 body.className = "";
}

light.onclick = function(){
 body.className = "light";
}


