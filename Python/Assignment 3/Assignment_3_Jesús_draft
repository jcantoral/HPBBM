#Assignment 3 HPBBM Draft - Jesus Cantoral
FASTAfile=open("Human_HRAS.fasta","r")
OutputFile=open("TranslateOutput.fasta","w")
DNASeq=[] #Defines a list that will contain DNASeq
LineCounter=0 #This will help avoid the first FASTA file line (i.e >(...) \n)
for Line in FASTAfile: #This for loop will read each FASTAfile line and will add it to the DNASeq list
    if LineCounter==0: #This is, only in the first line of FASTAfile
        LineCounter=LineCounter+1
        continue
    else:
        Line=Line.strip()
        DNASeq.append(Line.strip("\n")) #Add each line in FASTAfile to a DNASeq list
        counter=counter+1
        
DNASeq=list("".join(DNASeq)) #Forms a list joining all elements in DNASeq list.

GeneticCodeFile=open("GeneticCode_standard.csv","r")
Triplets,TripletsList,AAoneletter=[],[],[] #This structure is called a "tuple" in Python (say a,b,c = 1,2,3) and is written to save lines. These three lists will serve in following lines.

for Line in GeneticCodeFile: #Similarly when parsing the FASTA file, this loop creates not one but two lists (Triplets and AAoneletter).
    Triplets=Line.split("\t")
    TripletsList.append(Triplets[0])
    AAoneletter.append(Triplets[1])

GeneticCode=dict(zip(TripletsList,AAoneletter)) #These functions create a "Genetic Code" dictionary from two lists.

for Frame in range(3): #This loop will create three frames for the "forward" sequence and will translate each frame.
    Protein=""
    for NucPos in range(Frame,(len(DNASeq)-2),3):
        Protein=Protein+(GeneticCode.get(DNASeq[NucPos]+DNASeq[NucPos+1]+DNASeq[NucPos+2]))
    OutputFile.write("\n>\n"+Protein)

Nucleotides="ATGC" #"Forward" strand nucleotides
TransTable=str.maketrans(Nucleotides,"TACG") #Corresponding reverse complementary nucleotides
RevComp="".join(DNASeq[::-1]).translate(TransTable) #Declares a string that is reverse complementary (as nucleotides are complementary and inverted position).

for Frame in range(3): #Same philosophy as the previous "for" loop, but for the reverse complementary (antiparallel) sequence.
    Protein=""
    for NucPos in range(Frame,(len(RevComp)-2),3):
       Protein=Protein+(GeneticCode.get(RevComp[NucPos]+RevComp[NucPos+1]+RevComp[NucPos+2]))
    OutputFile.write("\n>\n"+Protein)
       
FASTAfile.close()
GeneticCodeFile.close()
OutputFile.close()
