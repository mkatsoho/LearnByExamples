#! /usr/bin/python3

import cherrypy		;# use cherrypy as web server and app server
import subprocess 	;# exec os command and get its output
 

class HelloWorld(object):
 
    @cherrypy.expose
    def index(self):
        return "Hello World!"
        
    @cherrypy.expose
    def runcmd(self):
        output = subprocess.check_output( "ls -la", shell=True)
        return '''
<html>
    <header>
    <title>run os command from web server</title>
    </header>
    <body>
	<pre> %s </pre>
	<p/>
	%s
    </body>
</html>
''' % (output, output)

    @cherrypy.expose
    def jsonOutput(self):
        return '''{"name":"Tony Zhu", Height:180}'''
        
        
        
    #index.exposed = True
    #tony.exposed = True
    #jsonOutput.exposed = True


conf_global = { 
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 7766,
    },
}

cherrypy.config.update(conf_global)
cherrypy.quickstart(HelloWorld())

