import nltk
from nltk import word_tokenize
from nltk import pos_tag
import datetime
import re
import MySQLdb

#Open sentence detector model
sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")
#Open notes file for reading
noteFile = open ('testing/test_data/set4/test_data.txt','r')
diagNerFileBigram = 'Training/output/13000/NER_Files/bigram/diagnosis_bigram.ner'
procNerFileBigram = 'Training/output/13000/NER_Files/bigram/procedure_bigram.ner'
vitalNerFileBigram = 'Training/output/13000/NER_Files/bigram/vital_bigram.ner'
diagNerFileBigramToRead = open (diagNerFileBigram,'r')
procNerFileBigramToRead = open (procNerFileBigram,'r')
vitalNerFileBigramToRead = open (vitalNerFileBigram,'r')
print "Processing note for bigram of file "+noteFile.name+"...."
noteCount = 0
sentCount=0
diagNerBigramCnt=0
procNerBigramCnt=0
vitalNerBigramCnt=0
startTime = datetime.datetime.now()
processedSentence =""
db = MySQLdb.connect(host ="localhost", user ="root", passwd = "root", db = "nlp")
cur = db.cursor()
tbl_name = "ner_bigrams"
setId  ="set4"
cur.execute("delete from "+tbl_name+" where set_id = %s",(setId))
for line in noteFile:
    sentCount = 0
    #print "Note Number ---->"+ str(noteCount)
    #print "Original note Text read from file\n"+line
    #Sentence Detection
    sentences = sentence_detector.tokenize(line.strip())
    for index in range (len(sentences)):
        #Preprocessing dictionary
        abbr ={' pt ':' patient ','Pt':'Patient',' dx ':' diagnosis ',' hx ':' history ','f/u':'follwup','n\'t':' not','appt':'appointment','meds':'medication','yrs':'years','wt':'weight','hsp':'hospital','malfx':'malfunction','unsat':'unsaturated','F/u':'Follow up','carbs':'carbohydrade','trigly ':'triglycerides ','trigly.':'triglycerides.',
               '-':' - ','.':' . ', 'n?t':' not','/':' / '}
        processedSentence = sentences[index].lower()
        #Preprocessing
        for k,v in abbr.items():
            processedSentence=processedSentence.replace(k,v)
        #print "sentence >>>"+processedSentence
        sentBigram = list(nltk.bigrams(processedSentence.split()))
        for i in range (0 , len(sentBigram)):
            #print "Bigram from input sent:"
            #print sentBigram[i]
            diagNerFileBigramToRead = open (diagNerFileBigram,'r')
            for diagBigrams in diagNerFileBigramToRead:
                diagNerBigram = list(nltk.bigrams(diagBigrams.split()))
                if len(diagNerBigram)==1:
                    if sentBigram[i]==diagNerBigram[0]:
                        #print "Match found Diag>>>>>"
                        #print sentBigram[i]
                        diagNerBigramCnt = diagNerBigramCnt + 1
                        noteId = "Note_Number-"+str(noteCount+1)+":"
                        word = sentBigram[i][0]+' '+sentBigram[i][1]
                        sentId = "Sent_Number-"+str(sentCount+1)+":"
                        matchedValue="diagnosis"
                        cur.execute("insert into "+tbl_name+" (note_id,detected_element,element_type,set_id,sent_id,updated_date) values(%s,%s,%s,%s,%s,%s)",
                            (noteId,word,matchedValue,setId,sentId,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
            procNerFileBigramToRead = open (procNerFileBigram,'r')
            for procBigrams in procNerFileBigramToRead:
                procNerBigram = list(nltk.bigrams(procBigrams.split()))
                if len(procNerBigram)==1:
                    if sentBigram[i]==procNerBigram[0]:
                        #print "Match found Proc >>>>>"
                        #print sentBigram[i]
                        procNerBigramCnt = procNerBigramCnt + 1
                        noteId = "Note_Number-"+str(noteCount+1)+":"
                        word = sentBigram[i][0]+' '+sentBigram[i][1]
                        sentId = "Sent_Number-"+str(sentCount+1)+":"
                        matchedValue="procedure"
                        cur.execute("insert into "+tbl_name+" (note_id,detected_element,element_type,set_id,sent_id,updated_date) values(%s,%s,%s,%s,%s,%s)",
                            (noteId,word,matchedValue,setId,sentId,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
            vitalNerFileBigramToRead = open (vitalNerFileBigram,'r')
            for vitalBigrams in vitalNerFileBigramToRead:
                vitalNerBigram = list(nltk.bigrams(vitalBigrams.split()))
                if len(vitalNerBigram)==1:
                    if sentBigram[i]==vitalNerBigram[0]:
                        #print "Match found vital >>>>>"
                        #print sentBigram[i]
                        vitalNerBigramCnt = vitalNerBigramCnt + 1
                        noteId = "Note_Number-"+str(noteCount+1)+":"
                        word = sentBigram[i][0]+' '+sentBigram[i][1]
                        sentId = "Sent_Number-"+str(sentCount+1)+":"
                        matchedValue="vital"
                        cur.execute("insert into "+tbl_name+" (note_id,detected_element,element_type,set_id,sent_id,updated_date) values(%s,%s,%s,%s,%s,%s)",
                            (noteId,word,matchedValue,setId,sentId,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
        sentCount = sentCount+1
    noteCount = noteCount+1
        #print sentBigram
        #print processedSentence   
#Dsiplays
noteFile.close()
diagNerFileBigramToRead.close()
procNerFileBigramToRead.close()
vitalNerFileBigramToRead.close()
print ("\nProcessing completed!!!")
endTime = datetime.datetime.now()
timeDiff =endTime-startTime
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
print ("\nTotal number of sentences detected :",sentCount)
print ("\nTotal number of notes detected :",noteCount)
print ("\nTotal diag bigrams detected :",diagNerBigramCnt)
print ("\nTotal prod bigrams detected :",procNerBigramCnt)
print ("\nTotal vital bigrams detected :",vitalNerBigramCnt)

                
