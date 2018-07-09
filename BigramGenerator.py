import nltk
import datetime

startTime = datetime.datetime.now()
diagNerFile = 'Training/output/13000/NER_Files/diagnosis.ner'
procNerFile='Training/output/13000/NER_Files/procedure.ner'
vitalNerFile='Training/output/13000/NER_Files/vital.ner'
diagNerFileToRead = open(diagNerFile,'r')
procNerFileToRead = open(procNerFile,'r')
vitalNerFileToRead = open(vitalNerFile,'r')
diagNerFileBigram = 'Training/output/13000/NER_Files/bigram/diagnosis_bigram.ner'
procNerFileBigram = 'Training/output/13000/NER_Files/bigram/procedure_bigram.ner'
vitalNerFileBigram = 'Training/output/13000/NER_Files/bigram/vital_bigram.ner'
diagNerFileBigramToWrite = open(diagNerFileBigram,'w')
procNerFileBigramToWrite = open(procNerFileBigram,'w')
vitalNerFileBigramToWrite = open(vitalNerFileBigram,'w')
diagBigramCount = 0
procBigramCount = 0
vitalBigramCount = 0
print "NER Bigram Generator Started............"
for line in diagNerFileToRead:
    diagBigramString = list(nltk.bigrams(line.split()))
    if len(diagBigramString)==1:
        diagNerFileBigramToWrite.write(line)
        diagBigramCount = diagBigramCount + 1
for line in procNerFileToRead:
    procBigramString = list(nltk.bigrams(line.split()))
    if len(procBigramString)==1:
        procNerFileBigramToWrite.write(line)
        procBigramCount = procBigramCount + 1
for line in vitalNerFileToRead:
    vitalBigramString = list(nltk.bigrams(line.split()))
    if len(vitalBigramString)==1:
        vitalNerFileBigramToWrite.write(line)
        vitalBigramCount = vitalBigramCount + 1
diagNerFileBigramToWrite.write('\n')
procNerFileBigramToWrite.write('\n')
vitalNerFileBigramToWrite.write('\n')
diagNerFileToRead.close()
diagNerFileBigramToWrite.close()
procNerFileToRead.close()
procNerFileBigramToWrite.close()
vitalNerFileToRead.close()
vitalNerFileBigramToWrite.close()
endTime = datetime.datetime.now()
timeDiff =endTime-startTime
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Diag NER Bigram Generator Completed............"
print "Total Diag Bigram Generated:"+str(diagBigramCount)
print "Total Proc Bigram Generated:"+str(procBigramCount)
print "Total Vital Bigram Generated:"+str(vitalBigramCount)
print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
