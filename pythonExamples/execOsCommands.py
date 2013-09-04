#! /usr/bin/python3


import subprocess	;# exec commands, which replaces other discard methods, e.g. `cmd`, os.system(args), os.spawnXX(), os.popenN()
### examples, referred to http://docs.python.org/2/library/subprocess.html#subprocess.Popen




## basic example - call, returns error_code
rtn = subprocess.call( ["ls", "-la"] )
print("# basic example - rtn=%s" % rtn)


## typical examples - shell=True (unsecure) | False (secure)
rtn = subprocess.call( "ls -la", shell=True )
print("# typical examples - shell is true, rtn=%s" % rtn)
rtn = subprocess.call( ["ls", "-la"], shell=False )
print("# typical examples - shell is false (secure mode), rtn=%s" % rtn)


## raise exception examples - reture rtn_code (check_out) | output (check_output)
try :
    rtn = subprocess.check_call( "ls_na -la", shell=True )
except subprocess.CalledProcessError as e:
    print( "# raise exception examples - check_call(), CalledProcessError as e: e.returncode=%s e.cmd=%s e.output=%s" % (e.returncode, e.cmd, e.output) )
print( "rtn=%s" % rtn )

output = ""	;# MUST declare this due to exception will break the assignment
try :
    output = subprocess.check_output( "ls -la", shell=True )
except subprocess.CalledProcessError as e:
    print( "# raise exception examples - check_output(), CalledProcessError as e: e.returncode=%s e.cmd=%s e.output=%s" % (e.returncode, e.cmd, e.output) )
print( "output=%s" % output )


## popen example - exec like output=`dmesg | grep hda`
p1 = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "hda"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]
print( "# Popen class example - output=%s" % output )



## get err output example - ???

