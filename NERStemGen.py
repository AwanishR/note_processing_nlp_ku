import nltk
import datetime
from nltk.stem.porter import PorterStemmer

startTime = datetime.datetime.now()
habitNerFile = 'Training/output/13000/NER_Files/habit.ner'
procNerFile='Training/output/13000/NER_Files/procedure.ner'
vitalNerFile='Training/output/13000/NER_Files/vital.ner'
habitNerFileToRead = open(habitNerFile,'r')
procNerFileToRead = open(procNerFile,'r')
vitalNerFileToRead = open(vitalNerFile,'r')
habitNerFileStem = 'Training/output/13000/NER_Files/stem/habit_stem.ner'
procNerFileBigram = 'Training/output/13000/NER_Files/bigram/procedure_bigram.ner'
vitalNerFileBigram = 'Training/output/13000/NER_Files/bigram/vital_bigram.ner'
habitNerFileStemToWrite = open(habitNerFileStem,'w')
procNerFileBigramToWrite = open(procNerFileBigram,'w')
vitalNerFileBigramToWrite = open(vitalNerFileBigram,'w')
diagBigramCount = 0
procBigramCount = 0
vitalBigramCount = 0
stemmer = PorterStemmer()
print "NER Stem Generator Started............"
for line in habitNerFileToRead:
    word = line.split()
    #print word
    #for l in range (0,len(word)):
    stemword =stemmer.stem(line.strip())
    habitNerFileStemToWrite.write(stemword+'\n')
    print "<<<<org word>>>"+line + "++++++stemmed word+++++"+stemword
'''for line in procNerFileToRead:
    procBigramString = list(nltk.bigrams(line.split()))
    if len(procBigramString)==1:
        procNerFileBigramToWrite.write(line)
        procBigramCount = procBigramCount + 1
for line in vitalNerFileToRead:
    vitalBigramString = list(nltk.bigrams(line.split()))
    if len(vitalBigramString)==1:
        vitalNerFileBigramToWrite.write(line)
        vitalBigramCount = vitalBigramCount + 1'''
habitNerFileStemToWrite.write('\n')
procNerFileBigramToWrite.write('\n')
vitalNerFileBigramToWrite.write('\n')
habitNerFileToRead.close()
habitNerFileStemToWrite.close()
procNerFileToRead.close()
procNerFileBigramToWrite.close()
vitalNerFileToRead.close()
vitalNerFileBigramToWrite.close()
habitfilenamenodups = 'Training/output/13000/NER_Files/stem/habit_stem_nodupe.ner'
habitNerFileStemToRead =open (habitNerFileStem,'r')
#--Remove dups from Habit corpus
habitCount =0

lines_seen = set() # holds lines already seen
outfile = open(habitfilenamenodups, "w")
for line in habitNerFileStemToRead:
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        habitCount = habitCount+1
outfile.write(">>Total Habits detected << " + str (habitCount))
outfile.close()

endTime = datetime.datetime.now()
timeDiff =endTime-startTime
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Diag NER Bigram Generator Completed............"
print "Total Diag Bigram Generated:"+str(diagBigramCount)
print "Total Proc Bigram Generated:"+str(procBigramCount)
print "Total Vital Bigram Generated:"+str(vitalBigramCount)
print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
