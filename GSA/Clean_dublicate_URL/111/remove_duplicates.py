import time
import hashlib
import sys
import re

distinct=set()
total=0;
dup=0
insert=0
excluded=0

pattern=re.compile("^\s*(https*:\/\/[^\/]*).*$")

print(time.ctime())

excludes = set(line.strip() for line in open('excludes.txt'))

print('Exclude: '+str(excludes))

if (len(sys.argv)<2):
    print('Error: Pass filename as script''s argument')
    sys.exit()

with open('distinct_'+sys.argv[1], "a") as writeToFile:
    with open(sys.argv[1]) as readFromFile:
        for line in readFromFile:

            total+=1
            m = re.match(pattern, line.strip())

            if m:
                domain = m.group(1)

                if any(exclude in domain for exclude in excludes):
                    excluded+=1
                    continue
                    
                if domain not in distinct:
                    writeToFile.write(domain+'\n')
                    distinct.add(domain)
                    insert+=1
                else:
                    dup+=1
                
            else:
#                print('Bad line: '+line)
                continue
            

print('Lines total: '+str(total))
print('Excluded: '+str(excluded))
print('Duplicates: '+str(dup))
print('Inserted: '+str(insert))

print(time.ctime())
