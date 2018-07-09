import nltk
from nltk import word_tokenize
from nltk import pos_tag
import datetime

#Open sentence detector model
sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")
#Open notes file for reading
noteFile = open ('testing/test_data/set3/test_data.txt','r')
#Opens output file for writing
fileToWrite = open("testing/output/set3/processednotes.txt","w")
#Opens tree bank file for writing
fileTreeBank  = open ("testing/output/set3/treeBank.txt","w+")
print "Processing note of file "+noteFile.name+"...."
noteCount = 1
tokenCount =0
sentCount=0
startTime = datetime.datetime.now()
for line in noteFile:
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
            #print (k,v)
        #print ("Original Sentence:++++"+str(noteCount)+">>>"+sentences[index])
        #print ("\nPreprocessed Sentence:---->"+processedSentence)
        fileToWrite.write("\n<< Note Number >>"+str(noteCount))
        fileToWrite.write("\nOriginal Sentence"+str(index+1)+" >>> "+sentences[index])
        fileToWrite.write("\nPreprocessed Sentence:>>>:"+processedSentence+" <<<\n\nTokens of this sentence are as follows\n")
        #fileTreeBank.write("\nOriginal Sentence"+str(index+1)+" >>> "+sentences[index])
        #fileTreeBank.write("\nPreprocessed Sentence:>>>:"+processedSentence+" <<<\n----POS Tagging---\n")
        #Tokenization
        tokens = word_tokenize(processedSentence)
        #POS Tagging [PennTreebank tagger]
        postag=pos_tag(tokens);
        #Write tokens into file
        for item in tokens:
            fileToWrite.write("\n----\n{}".format(item))
            tokenCount+=len(item)
        fileToWrite.write("\n*****POS Tagging [using Penn Treebank tagging]****\n")
        #Write POS tag in file
        for item in postag:
            fileToWrite.write("{} ".format(item))
            fileTreeBank.write("{}".format(item))
        fileToWrite.write("\n")
    fileTreeBank.write("\n")
        #Write in tree  bank
        ##for index in range (len(postag)):
            ##fileTreeBank.write("\n"+str(postag[index]))
            #print ("\n"+str(postag[index]))
    sentCount+=len(sentences)
    noteCount = noteCount+1
fileTreeBankRead  = open ("testing/output/set3/treeBank.txt","r")
#print("new file -----------",fileTreeBankRead.name)
'''for lines in fileTreeBankRead:
     print ("line****",lines)'''
fileTreeBankRead.close()
fileToWrite.close()
fileTreeBank.close()
#Dsiplays
noteFile.close()
print ("\nProcessing completed!!!")
endTime = datetime.datetime.now()
timeDiff =endTime-startTime
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
print ("\nTotal number of sentences detected :",sentCount)
print("\nTotal number of tokens detected :",tokenCount)

                
