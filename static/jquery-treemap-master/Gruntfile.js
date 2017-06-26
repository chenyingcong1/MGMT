module.exports = function(grunt) {
    grunt.initConfig({
        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            all: [
              'js/jquery.treemap.js'
            ]
        },
        uglify: {
            target: {
                files: {
                    'js/dist/jquery.treemap.min.js': ['js/jquery.treemap.js']
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('build', [
        'jshint',
        'uglify'
    ]);

    grunt.registerTask('default', ['build']);
};
