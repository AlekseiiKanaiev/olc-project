// import { Stream } from "stream";

var gulp            = require("gulp"),
    sass            = require("gulp-sass"),
    browserSync     = require("browser-sync"),
    concat          = require("gulp-concat"), 
    uglify          = require("gulp-uglify"),
    cleanCSS        = require("gulp-clean-css"),
    rename          = require("gulp-rename"),
    del             = require("del"),
    imgmin          = require("gulp-imagemin"),
    pngquant        = require("imagemin-pngquant"),
    cache           = require("gulp-cache"),
    autoprefixer    = require("gulp-autoprefixer") ;
    // watch   = require("gulp-watch");

gulp.task("sass", function(){
    return gulp.src("./app/static/sass/**/*.sass")
    .pipe(sass().on("error", sass.logError))
    .pipe(autoprefixer(["last 15 versions", "> 1%", "ie 8", "ie 7"], {cascade:true}))
    .pipe(gulp.dest("./app/static/css"))
    .pipe(browserSync.reload({stream:true})) ;
});

gulp.task("scripts", function(){
    return gulp.src([
        "./app/static/libs/jquery/dist/jquery.min.js",
        "./app/static/libs/magnific-popup/dist/jquery.magnific-popup.min.js",
        // "./app/static/libs/popper.js/dist/umb/popper.min.js",
        "./app/static/libs/bootstrap/dist/js/bootstrap.bundle.min.js",
        "./app/static/libs/background-video/jquery.backgroundvideo.min.js",
        "./app/static/libs/device.js/lib/device.min.js",
        "./app/static/libs/owl.carousel/dist/owl.carousel.min.js",
        "./app/static/fonts/fontawesome/fontawesome-all.js"
    ])
    .pipe(concat("libs.min.js"))
    .pipe(uglify())
    .pipe(gulp.dest("./app/static/js")) ; 
});

gulp.task("css-min", ["sass"], function(){
    return gulp.src("./app/static/css/main.css")
    .pipe(cleanCSS())
    .pipe(rename({suffix:".min"}))
    .pipe(gulp.dest("./app/static/css"))
});

gulp.task("img", function(){
    return gulp.src("./app/static/img/**/*")
    .pipe(cache(imgmin({
        interlaced: true,
        progressive: true,
        svgoPlugins: [{
            removeViewBox: false
        }],
        use:[pngquant()]
    })))
    .pipe(gulp.dest("./dist/static/img"))
});

gulp.task("browser-sync", function(){
    browserSync({
        server: {
            baseDir: "./app",
            index: "./templates/g-index.html"
        },
        notify: false
    });
});

gulp.task("clean", function(){
    return del.sync("./dist");
});

gulp.task("clear", function(){
    return cache.clearAll();    
});

gulp.task("watch", ["browser-sync", "css-min", "scripts"],
    function(){
    gulp.watch("./app/static/sass/**/*.sass", ["css-min"]);
    gulp.watch("./app/static/js/**/*.js", browserSync.reload);
    gulp.watch("./app/**/*.html", browserSync.reload);
});

gulp.task("build", ["clean", "img", "css-min", "scripts"],
    function(){
        var buildCSS = gulp.src([
                "./app/static/css/main.css",
                "./app/static/css/libs.min.css"
            ])
            .pipe(gulp.dest("./dist/static/css"))
        
        var buildFonts = gulp.src("./app/static/fonts/**/*")
            .pipe(gulp.dest("./dist/static/fonts"))

        var buildJS = gulp.src("./app/static/js/**/*.js")
            .pipe(gulp.dest("./dist/static/js"))

        var buildHtml = gulp.src("./app/templates/*.html")
            .pipe(gulp.dest("./dist/templates"));
});
