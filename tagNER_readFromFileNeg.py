import datetime
#from datetime import datetime
import MySQLdb
#from time import gmtime, strftime
prefix = 'Training/output/13000/NER_Files/'
habitnerfile='habit.ner'
diagnerfile='diagnosis.ner'
procnerfile='procedure.ner'
drugnerfile='drug.ner'
vitalnerfile = 'vital.ner'
nounInFile = 'testing/output/set4/neg_nnvb.txt'
finalOutputFile = 'Testing/output/set4/13000/NER_Output/neg_finalout.tx'
totalMatch =0
def tagmedterm(text):
    fhabit=open(prefix+habitnerfile,'r')
    fdiag=open(prefix+diagnerfile,'r')
    fproc=open(prefix+procnerfile,'r')
    fdrug=open(prefix+drugnerfile,'r')
    fvital=open(prefix+vitalnerfile,'r')
    global totalMatch
    match = 'no match xx'
    #print text
    for line in fhabit:
        #print line
        #print "in habit"
        if text.lower() == line.rstrip().lower():
            match=habitnerfile[:habitnerfile.find(".")]
            totalMatch = totalMatch+1
            break
    for line1 in fdiag:
        #print line1
        #print "in diag"
        if text.lower() == line1.rstrip().lower():
            match=diagnerfile[:diagnerfile.find(".")]
            totalMatch = totalMatch+1
            break
    for line2 in fproc:
        #print line2
        #print "in proc"
        if text.lower() == line2.rstrip().lower():
            match = procnerfile[:procnerfile.find(".")]
            totalMatch = totalMatch+1
            break
    for line3 in fdrug:
        #print line3
        #print "in drug"
        if text.lower() == line3.rstrip().lower():
            match = drugnerfile[:drugnerfile.find(".")]
            break
    for line3 in fvital:
        #print line3
        #print "in drug"
        if text.lower() == line3.rstrip().lower():
            match = vitalnerfile[:vitalnerfile.find(".")]
            totalMatch = totalMatch+1
            break
    fhabit.close()
    fdiag.close()
    fproc.close()
    fdrug.close()
    fvital.close()
    return match

def main():
    db = MySQLdb.connect(host ="localhost", user ="root", passwd = "root", db = "nlp")
    cur = db.cursor()
    startTime = datetime.datetime.now()
    tbl_name = "ner_neg"
    print "Processing NER matcher ..."
    nounFile = open(nounInFile,'r')
    ffinal = open (finalOutputFile,'w')
    noteId = "0"
    sentId="0"
    setId = "set4"
    cur.execute("delete from "+tbl_name+" where set_id = %s",(setId))
    for line in nounFile:
        words = line.split()
        for word in words:
            if "Note_Number" not in word and "Sent_Number" not in word:
                #print "Detected Noun::"+word
                #print word+" is "+ tagmedterm(word)
                matchedValue = tagmedterm(word)
                ffinal.write("Detected NN-VB::"+word+"\n")
                ffinal.write(word+" is "+ matchedValue+"\n")
                cur.execute("insert into "+tbl_name+" (note_id,detected_element,element_type,set_id,sent_id,updated_date) values(%s,%s,%s,%s,%s,%s)",
                            (noteId,word,matchedValue,setId,sentId,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
            else:
                ffinal.write("\n"+word)
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
