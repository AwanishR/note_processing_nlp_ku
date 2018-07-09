import nltk
from nltk import word_tokenize
from nltk import pos_tag
import re
import datetime

#Open sentence detector model
sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")
#Open notes file for reading
#noteFile = open ('testing/test_data/test_data.txt','r')
#Opens output file for writing
#fileToWrite = open("testing/output/processednotes.txt","w")
#Opens tree bank file for writing
#fileTreeBank  = open ("testing/output/treeBank.txt","w+")
#print "Processing note of file "+noteFile.name+"...."
#noteCount = 1
#tokenCount =0
#sentCount=0
verbCount=0
startTime = datetime.datetime.now()
print "NN-VB extractor running ..."
fileTreeBankRead  = open ("testing/output/set4/treeBank.txt","r")
verbOutFile = open ("testing/output/set4/nnvb.txt","w")
noteNum = 1
#print("new file -----------",fileTreeBankRead.name)
for line in fileTreeBankRead:
     #print ("line****",line)
     noteStartPos= line.find("NoteID")
     noteEndPos= line.find (")(Sent")
     noteNums=line[noteStartPos+7:noteEndPos]
     sentStartPos = line.find("SentID")
     sentEndPos = len(line)
     sentNum = line[sentStartPos+7:sentEndPos-2]
     #print noteNum;
     verbOutFile.write("Note_Number-"+ noteNums+": ")
     verbOutFile.write("Sent_Number-"+ sentNum+": ")
     for m in re.finditer("\(",line):
        #print m
        l1=line[m.start():len(line)]
        #print "find ---->>" + m.rfind(',',0)
        #print (l1)
        startPos=l1.find("(")
        endPos=l1.find(")")
        l2=l1[startPos:endPos]
        #print l1[startPos:endPos]
        #print "find (---"+str(startPos)
        #print "find )---"+str(endPos)
        #print l2
        if "VB" in l2 or "NN" in l2:
             startPos1=l2.find("(")
             endPos1=l2.find(",")
             #print "find 1 ----"+ str(startPos1)
             #print "find 2 -----"+str(endPos1)
             l3=l2[startPos1+2:endPos1-1]
             #print (l3)
             verbOutFile.write(l3.lower()+"\t")
             verbCount = verbCount + 1
        #print ("Noun detected "+l2[::-1])
        #nounOutFile.write(l2+"\t")
        #diag=l2.lstrip()
        #print habit
        #diagCorpus = open (diagfilename,'a')
        #diagCorpus.write(diag.strip().lower()+"\n")                        
        #diagCorpus.close()
     verbOutFile.write ("\n")   
     noteNum=noteNum+1
fileTreeBankRead.close()
verbOutFile.close()
endTime = datetime.datetime.now()
timeDiff =endTime-startTime
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
print ("\nNoun-Verb extraction completed!!!")
print "Total Noun-Verb extracted::"+str(verbCount)


                
