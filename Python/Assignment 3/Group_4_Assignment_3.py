#Assignment 3 - Group 4 -- Jesus Cantoral, Alberto Ferrera, Leticia Rodriguez
# Opening the FASTA Sequence
SeqFile=open("Human_HRAS.fasta",'r')

Seq=[]
for Line in SeqFile:
    if '>' in Line:
        Line=Line      #It ignores the first line, with the name of the sequence in FASTA
    else:               
           #It removes \n
        LineSeq=Line.strip()
        Seq.append(LineSeq)    #It adds each line to the list Seq
     
Seq=''.join(Seq)        #To join every line in one seq line

 #Reading the genetic code               
Codons=[]
AA=[]
MyCode=open("GeneticCode_standard.csv","r")
for Line in MyCode:          
    Line=Line.strip()
    GeneticCode=Line.split("\t")
    Codons.append(GeneticCode[0])
    AA.append(GeneticCode[1])
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
OutputFile=open("Protein_translation.fasta","w")

OutputFile.write(">Protein 1st ORF:\n"+"".join(Prot1)+"\n\n")
OutputFile.write(">Protein 2nd ORF:\n"+"".join(Prot2)+"\n\n")
OutputFile.write(">Protein 3rd ORF:\n"+"".join(Prot3)+"\n\n")
OutputFile.write(">Protein 4th ORF:\n"+"".join(Prot4)+"\n\n")
OutputFile.write(">Protein 5th ORF:\n"+"".join(Prot5)+"\n\n")
OutputFile.write(">Protein 6th ORF:\n"+"".join(Prot6)+"\n\n")
print("Script ended. Output file is Protein_translation.fasta")
OutputFile.close()    #Closing all files.
MyCode.close() 
SeqFile.close()
