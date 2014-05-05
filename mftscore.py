oldline = []
newline = []

#read stats file
f = open('mftscore.txt')
lines = f.readlines()
f.close()

#break new file and old file
for line in lines:
    if line.startswith('589'):
        oldline.append(line)
    else:
        newline.append(line)

f = open('oldScoreupload.txt','w')
for o in oldline:
    f.write(o) # python will convert \n to os.linesep
f.close()


f = open('newfile.txt','w')
for n in newline:
    f.write(n) # python will convert \n to os.linesep
f.close()


#take new file and put it in insert sql statement
f = open('newsql.txt','w')
for n in newline:
    x = n.replace(',','').replace(':','\',\'').rstrip()
    x = '{0}{1}{2}'.format('insert into temptable (\'',x,'\')\n')
    f.write(x) # python will convert \n to os.linesep
f.close()
    
#do SQL join replaceID and upload