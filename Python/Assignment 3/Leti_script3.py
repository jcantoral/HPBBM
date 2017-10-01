# Opening the FASTA Sequence
SeqFile=open("Human_HRAS.fasta.txt",'r')

#Reading the FASTA Sequence
for Line in SeqFile:         #Some parsing of the file so we get only the sequence.
    MyData=SeqFile.readlines()
    Seq="".join(MyData)
    Seq=Seq.replace("\n","")

 #Reading the genetic code               
Codons=[]
AA=[]
MyCode=open("GeneticCode_standard.csv","r")
for Line in MyCode:          
    Line=Line.strip()
    GeneticCode=Line.split("\t")
    Codons.append(GeneticCode[0])
    AA.append(GeneticCode[2])
Dictionary=dict(zip(Codons,AA)) #We are creating a dictionary in which the codons are the keys, and the aa are the values.

#Getting the reverse complement
Original_Symbols="ACTG"
Complementaries="TGAC"
TransTable=str.maketrans(Original_Symbols,Complementaries)
NewSeq=Seq.translate(TransTable)
Reverse_Complement=NewSeq[::-1]

#Getting the 6 ORFs and translating
Prot1=[]
Prot2=[]
Prot3=[]

for i in range(0,len(Seq),3): #We are separating the Sequence in its codons, and the for each codon we are taking its value from the dictionary and adding it to a new list.
    Prot1.append(Dictionary[Seq[i:i+3]])
    if i+1>(len(Seq)-3):      #This way we don't have incomplete codons at the end.
            break
    Prot2.append(Dictionary[Seq[i+1:i+4]])
    Prot3.append(Dictionary[Seq[i+2:i+5]])

Prot4=[]
Prot5=[]
Prot6=[]

for k in range(0,len(Reverse_Complement),3):
    Prot4.append(Dictionary[Reverse_Complement[k:k+3]])
    if k+1>(len(Reverse_Complement)-3):
            break
    Prot5.append(Dictionary[Reverse_Complement[k+1:k+4]])
    Prot6.append(Dictionary[Reverse_Complement[k+2:k+5]])

#Printing output in a new file    
OutputFile=open("Protein_translation.txt","w")

OutputFile.write("Your sequence is:"+ Seq+"\n")
OutputFile.write("Its reverse complement is:"+Reverse_Complement+"\n")
OutputFile.write("Protein1,1st ORF:"+"-".join(Prot1)+"\n")
OutputFile.write("Protein2,2nd ORF:"+"-".join(Prot2)+"\n")
OutputFile.write("Protein3,3rd ORF:"+"-".join(Prot3)+"\n")
OutputFile.write("Protein4,4th ORF:"+"-".join(Prot4)+"\n")
OutputFile.write("Protein5,5th ORF:"+"-".join(Prot5)+"\n")
OutputFile.write("Protein6,6th ORF:"+"-".join(Prot6)+"\n")

OutputFile.close()    #Closing all files.
MyCode.close() 
SeqFile.close()
