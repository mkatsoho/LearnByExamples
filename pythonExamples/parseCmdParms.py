#! /usr/bin/python3


import shlex	;# parse a command parameters, with taking care of parm like -key="va lue"
### examples, referred to http://docs.python.org/2/library/shlex.html



cmdLines = [
   r'cmd -key value',  
   r'cmd -key va lue',  
   r'cmd -key "va lue"',  
   r'cmd -key "va\"lue"',  
   r'cmd -key "va\'lue"',  
]

for cmdLine in cmdLines :
    result = shlex.split( cmdLine )
    print("# cmdLine=%s - parse result=%s " % ( cmdLine, result ) )


