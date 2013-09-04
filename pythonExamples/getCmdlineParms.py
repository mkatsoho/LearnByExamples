#! /usr/bin/python3


import sys	;# get the command line parameters, e.g. ./thisExample.py var1 var2 var3


print("# E.g. run this .py script - %s var1 var2" % sys.argv[0] ) 
print("# get cmdLine parms - argv#=%s, cmd=%s, argv=%s,"  % ( len(sys.argv), sys.argv[0], sys.argv[:] ) )


