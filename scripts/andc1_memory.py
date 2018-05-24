import os
import commands

memory = commands.getoutput("""free -t -m | grep "Total" | awk '{ print "Total (Inc Swap) : "$2" MB >> " "Used : "$3" MB >> Free : "$4" MB";}'""")

print memory
