import re
import datetime
trainfilename = 'input/training_data/15000/en-ner-medical.txt'
habitfilename = 'output/15000/temp/habittemp.ner'
habitfilenamenodups = 'output/15000/NER_Files/habit.ner'
procfilename = 'output/15000/temp/proceduretemp.ner'
procfilenamenodups = 'output/15000/NER_Files/procedure.ner'
diagfilename = 'output/15000/temp/diagnosistemp.ner'
diagfilenamenodups = 'output/15000/NER_Files/diagnosis.ner'
drugfilename = 'output/15000/temp/drugtemp.ner'
drugfilenamenodups = 'output/15000/NER_Files/drug.ner'
vitalfilename = 'output/15000/temp/vitaltemp.ner'
vitalfilenamenodups = 'output/15000/NER_Files/vital.ner'
fileToRead  =    open (trainfilename,'r')
habitCorpus =    open (habitfilename,'w')
procCorpus  =    open (procfilename,'w')
diagCorpus  =    open (diagfilename,'w')
drugCorpus  =    open (drugfilename,'w')
vitalCorpus =    open (vitalfilename,'w')
notecount   = 0
print "Training Started ....."
startTime = datetime.datetime.now()
for line in fileToRead:
    #HABIT Corpus
    for m in re.finditer("<START:habit",line):
        """print ("Habit found",m.start()) """
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(">")+1:l1.find("<")]
        habit=l2.lstrip()
        #print habit
        habitCorpus = open (habitfilename,'a')
        habitCorpus.write(habit.strip().lower()+"\n")                        
        habitCorpus.close()
        
    #PROCEDURE Corpus
    for m in re.finditer("<START:procedure",line):
        """print ("Habit found",m.start()) """
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(">")+1:l1.find("<")]
        proc=l2.lstrip()
        #print habit
        procCorpus = open (procfilename,'a')
        procCorpus.write(proc.strip().lower()+"\n")                        
        procCorpus.close()
        
    #DIAG Corpus
    for m in re.finditer("<START:diagnosis",line):
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(">")+1:l1.find("<")]
        diag=l2.lstrip()
        #print habit
        diagCorpus = open (diagfilename,'a')
        diagCorpus.write(diag.strip().lower()+"\n")                        
        diagCorpus.close()
        
    #DRUG Corpus
    for m in re.finditer("<START:drug",line):
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(">")+1:l1.find("<")]
        drug=l2.lstrip()
        #print habit
        drugCorpus = open (drugfilename,'a')
        drugCorpus.write(drug.strip().lower()+"\n")                        
        drugCorpus.close()

    #VITAL Corpus
    for m in re.finditer("<START:vital",line):
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(">")+1:l1.find("<")]
        vital=l2.lstrip()
        #print habit
        vitalCorpus = open (vitalfilename,'a')
        vitalCorpus.write(vital.strip().lower()+"\n")                        
        vitalCorpus.close()
    notecount=notecount+1
procCount=0
vitalCount = 0
diagCount = 0
habitCount =0
drugCount = 0
#--Remove dups from Procedure corpus
lines_seen = set() # holds lines already seen
outfile = open(procfilenamenodups, "w")
for line in open(procfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        procCount = procCount+1
outfile.write(">>Total Procedures detected << " + str (procCount))
outfile.close()
#--Remove dups from Habit corpus
lines_seen = set() # holds lines already seen
outfile = open(habitfilenamenodups, "w")
for line in open(habitfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        habitCount = habitCount+1
outfile.write(">>Total Habits detected << " + str (habitCount))
outfile.close()
#--Remove dups from Diagnosis corpus
lines_seen = set() # holds lines already seen
outfile = open(diagfilenamenodups, "w")
for line in open(diagfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        diagCount = diagCount+1
outfile.write(">>Total Diagnosis detected << " + str (diagCount))            
outfile.close()
#--Remove dups from drug corpus
lines_seen = set() # holds lines already seen
outfile = open(drugfilenamenodups, "w")
for line in open(drugfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        drugCount = drugCount+1
outfile.write(">>Total Drugs detected << " + str (drugCount))      
outfile.close()
#--Remove dups from vital corpus
lines_seen = set() # holds lines already seen
outfile = open(vitalfilenamenodups, "w")
for line in open(vitalfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        vitalCount = vitalCount+1
outfile.write(">>Total Vitals detected << " + str (vitalCount)) 
outfile.close()
print "Training Ended !!"
endTime = datetime.datetime.now ()
print "Total Training notes->" + str (notecount)
timeDiff =endTime-startTime
#datetime.timedelta(0, 8, 562000)
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Total Time taken to train " + str(notecount)+" notes is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
print ">>Total Procedure detected << " + str (procCount)
print ">>Total Diagnosis detected << " + str (diagCount)
print ">>Total Drugs detected << " + str (drugCount)
print ">>Total Habits detected << " + str (habitCount)
print ">>Total Vitals detected << " + str (vitalCount)
