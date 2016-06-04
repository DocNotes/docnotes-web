module.exports = function(grunt) {

    grunt.initConfig({

    // Directories
    srcDir:{
        base: 'build',

        // Source build directory: Global
		jade: 'build/jade',
        sass: 'build/sass',
        image: 'build/images'
    },

    distDir:{
        base: 'docnotes',

        // Destination public directory: Global
		view: 'templates',
        css: 'templates/css',
        image: 'templates/images'
    },

    // Tasks & Configurations

	// Task no. 1: Jade
	jade: {
		compile: {
			options: {
				basedir: '<%= srcDir.jade %>',
				pretty: true,
				compileDebug: true,
				wrap: false
			},
			files: [{
				expand: true,
				cwd: '<%= srcDir.jade %>',
				src: ['**/*.jade'],
				dest: '<%= distDir.view %>',
				ext: '.html'
			}]
		}
	},

    // Task no. 2: Sass
    sass:{
        options:{
            style: 'compressed', // Sass file style
            noCache: false, // Disable the noCache
            cacheLocation: 'temp/sass', // Cached sass location
            update: true // Only compile changed files
        },
        dist:{
            files:[{
                expand: true,
                cwd: '<%= srcDir.sass %>',
                src: '**/*.{sass,scss}',
                dest: '<%= distDir.css %>',
                ext:'.css'
            }]
        },
    },

    // Task no. 3: Image
    image:{
        dynamic:{
            files:[{
                expand: true,
                cwd: '<%= srcDir.image %>',
                src: ['**/*.{png,jpg,gif,svg}'],
                dest: '<%= distDir.image %>'
            }]
        },
    },

    // Task no. 4: Watch
    watch:{
        options:{
            spawn: false,
            livereload: true
        },
		jade: {
			files: '<%= srcDir.jade %>/**/*.jade',
			tasks: ['jade']
		},
		sass: {
			files: '<%= srcDir.sass %>/**/*.{scss,sass}',
			tasks: ['sass']
		}
    }

    });

    // Combined Tasks

    // Deployment
    grunt.registerTask('deploy',['jade', 'sass', 'image']);

    //Default
    grunt.registerTask('default',['watch']);

    // Depenent plugins
	grunt.loadNpmTasks('grunt-contrib-jade');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-image');
    grunt.loadNpmTasks('grunt-contrib-watch');

};
