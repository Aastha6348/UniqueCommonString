# including a Conatiner data type to handle data
import collections

# reading Input file
infile = open("data.txt")
data=infile.read()
listdata= data.splitlines()

# initializing
words = collections.Counter()
sublist=[]
flattened_list = []
common=[]
common_list=[]

# string to list processing for getting the entire string in 1 data container
for i in range(len(listdata)):
    sublist.append(listdata[i].split(' '))
for x in sublist:
    for y in x:
        flattened_list.append(y)

infile.seek(0)

# handling the word count
for line in infile:
    words.update(line.split())

for word, count in words.iteritems():
    if(len(listdata)>1):
        if(count>=len(listdata)):
            #creating the common list
            common.append(word)

#creating the common list
unique_list = [
    e
    for i, e in enumerate(flattened_list)
    if flattened_list.index(e) == i
]
#ordering the common list
for i in flattened_list:
    for j in common:
        if(j==i):
            if(j not in common_list):
                common_list.append(j)
            else:
                pass
        else:
            pass

# output processing
print 'Common List: ' + ' '.join(common_list)
print 'Unique List: ' + ' '.join(unique_list)