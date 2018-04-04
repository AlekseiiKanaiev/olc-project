$(document).ready(function(){
    if (!device.mobile() && !device.tablet()){
        var videobackground = new $.backgroundVideo($('.my-header'), {
            "align": "centerXY",
            "width": 1980,
            "height": 1200,
            "path": "static/video/",
            "filename": "Site teaser",
            "types": ["mp4","ogg","webm"],
            "preload": true,
            "autoplay": true,
            "loop": true
        });
        
    }
    else{
        $(".carousel").css({display:"block"});
        $(".descripton").css({display:"none"})
    }
        

    $('.dropdown').hover(
        function(){
            $(".dropdown-menu", this).stop(true, true).slideDown().addClass("show")
        },
        function(){
            $(".dropdown-menu", this).stop(true, true).slideUp("fast").removeClass("show")
        }
    );

    $(".nav-item").click(function(){
        $(this).parent().find(".active").removeClass("active");
        $(".nav-link", this).addClass("active");
    });

    $(".carousel").carousel({
        interval: 5000
    });

    // var video = document.getElementById("tiser");
    // video.loop = true;

});
