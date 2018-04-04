$(document).ready(function(){
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
        var div = '<div class="description d-none d-lg-block"><h1>Послуги з відеозйомки,<br/> фотозйомки та оренди</h1></div>'
        $(".my-header").append(div)
        $(".my-header").css("height", "100vh")
        // var height = $(".my-header-top").css("height")
        // console.log(height)
        // $(".description").css("max-height", height)
        $(".carousel").addClass("d-lg-none")
    }else{
        $(".carousel").removeClass("d-lg-none")
        $(".my-header").css("height", "auto")

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
