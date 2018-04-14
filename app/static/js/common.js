$(document).ready(function(){
    //define language 
    var lang = $(".lang").find(".active").attr("id")
    // changeLang(lang)

    //video-tiser
    if (!device.tablet() && !device.mobile()){
        var videobackground = new $.backgroundVideo($('.my-header'), {
            "align": "centerXY",
            "width": 1280,
            "height": 720,
            "path": "static/video/",
            "filename": "Site teaser",
            "types": ["mp4","ogg","webm"],
            "preload": true,
            "autoplay": true,
            "loop": true
        });

        $("#video_background").css("position", "absolute")

        var div = (lang === "ukr")?
        '<div class="description d-none d-lg-block"><div class = "ukr"><h1>Послуги з відеозйомки,<br/> фотозйомки та оренди</h1></div></div>'
        :'<div class="description d-none d-lg-block"><div class = "rus"><h1>Услуги видеосъёмки,<br/> фотосъёмки и аренды</h1></div></div>'
        $(".my-header").append(div)
        $(".my-header").css("height", "100vh")
        $("#my-carousel").addClass("d-lg-none")
    }else{
        $("#my-carousel").removeClass("d-lg-none")
        $(".my-header").css("height", "auto")
    }
    
    //seting dropdown-menu
    $('.dropdown').hover(
        function(){
            $(".dropdown-menu", this).stop(true, true).slideDown().addClass("show")
        },
        function(){
            $(".dropdown-menu", this).stop(true, true).slideUp("fast").removeClass("show")
        }
    );

    //setting active link
    $(".nav-item").click(function(){
        $(this).parent().find(".active").removeClass("active");
        $(".nav-link", this).addClass("active");
    });

    //init top carousel
    $("#my-carousel").carousel({
        interval: 5000
    });
    //init and seting team carousel
    $("#team-carousel").owlCarousel({
        loop:true,
        nav:true,
        dots:false,
        smartSpeed:700,
        navText:[
            '<i class="fas fa-angle-left"></i>',
            '<i class="fas fa-angle-right"></i>'
        ],
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                nav:true
            },
            738:{
                items:2,
                nav:true
            }
        }
    })
    
    if ($(".page-link:contains('None')")){
        $(".page-link:contains('None')").text("...").removeAttr("href")

    }

    //seting to-top button
    $(window).scroll(function(){
        if ($(this).scrollTop() > $(this).height()/2){
            $(".to-top").addClass("active")
        }else{
            $(".to-top").removeClass("active")
        }
    })
    $(".to-top").click(function(){
        $("html, body").stop().animate({scrollTop:0}, "slow", "swing")
    })

    // seting preloader
    $("header").ready(function(){
        $(".preloader").delay(500).fadeOut("fast")
    })

});

//func to change lang without reload
function changeLang(lang){
    console.log(lang)
    if (lang === "ukr"){
        $(".ukr").removeClass("d-none")
        $(".rus").addClass("d-none")
    }else{
        $(".ukr").addClass("d-none")
        $(".rus").removeClass("d-none")
    }
}