import datetime
#from datetime import datetime
import MySQLdb
from nltk.stem.porter import PorterStemmer
#from time import gmtime, strftime
prefix = 'Training/output/13000/NER_Files/'
habitnerstemfile='stem/habit_stem_nodupe.ner'
nounInFile = 'testing/output/set4/nnvb.txt'
finalOutputFile = 'Testing/output/set4/13000/NER_Output/finalout_habit_stem.txt'
totalMatch =0
def tagmedterm(text):
    fhabit=open(prefix+habitnerstemfile,'r')
    global totalMatch
    match = 'no match xx'
    #print text
    for line in fhabit:
        #print line
        #print "in habit"
        if text.lower() == line.rstrip().lower():
            match="habit"
            totalMatch = totalMatch+1
            break
    fhabit.close()
    return match

def main():
    stemmer = PorterStemmer()
    db = MySQLdb.connect(host ="localhost", user ="root", passwd = "root", db = "nlp")
    cur = db.cursor()
    startTime = datetime.datetime.now()
    tbl_name = "ner_stem"
    print "Processing Stem NER matcher ..."
    nounFile = open(nounInFile,'r')
    ffinal = open (finalOutputFile,'w')
    noteId = "0"
    sentId="0"
    setId = "set4"
    cur.execute("delete from "+tbl_name+" where set_id = %s",(setId))
    for line in nounFile:
        words = line.split()
        for word in words:
            ps = stemmer.stem(word)
            if "Note_Number" not in word and "Sent_Number" not in word:
                print "Detected Noun::"+word
                print "Stemmed word is:"+ps
                print word+" is "+ tagmedterm(ps)
                matchedValue = tagmedterm(ps)
                ffinal.write("Detected NN-VB::"+word+"\n")
                ffinal.write(word+" is "+ matchedValue+"\n")
                cur.execute("insert into "+tbl_name+" (note_id,detected_element,element_type,set_id,sent_id,updated_date) values(%s,%s,%s,%s,%s,%s)",
                            (noteId,word,matchedValue,setId,sentId,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
            else:
                ffinal.write("\n"+word+"==> Stemmed word>>"+ps)
                if "Note_Number" in word:
                    noteId=word
                if "Sent_Number" in word:
                    sentId = word
    print "in main"
    nounFile.close()
    print "NER matcher completed..."
    endTime = datetime.datetime.now()
    timeDiff =endTime-startTime
    formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
    print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
    print "Total match found::"+str(totalMatch)
if __name__=="__main__":
    main()
