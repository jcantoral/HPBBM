#Assignment 3
#Ferrera, A

#Open the files to read
SeqFile=open('Human_HRAS.fasta.txt','r')
GeneticCodeFile=open('GeneticCode_standard.csv','r')

#print(SeqFile.readlines())

#Print the sequence
Seq=[]
for Line in SeqFile:
    if '>' in Line:
        Line=Line      #It ignores the first line, with the name of the sequence in FASTA
    else:               
           #It removes \n
        LineSeq=Line.strip()
        Seq.append(LineSeq)    #It adds each line to the list Seq
     
Seq=''.join(Seq)        #To join every line in one seq line
print('The cDNA sequence is:\n\n',Seq)
        

#Preparing the genetic code dictionaries (one for 1 Letter, one for 2 Letters)
AA_1Letter=[]
AA_3Letters=[]
Codons=[]
for Line in GeneticCodeFile:
    Line=Line.split()                           #Split the genetic code into the codons and the aminoacids
    Codons.append(Line[0])
    AA_1Letter.append(Line[1])
    AA_3Letters.append(Line[2])
GeneticCode_1Letter=dict(zip(Codons,AA_1Letter))    #Convert the both lists in a dictionary to relate codons and aminoacids
GeneticCode_3Letters=dict(zip(AA_3Letters,Codons))
#print('\n',GeneticCode_1Letter)
#print('\n',GeneticCode_3Letters)


#Translations

##Stablishment of ORFs
ORF1=[]
ORF2=[]
ORF3=[]

c=0
while c<=100:                   #Generate three lists of nucleotic position, one for each ORF
   ORF1.append(c)
   ORF2.append(c+1)
   ORF3.append(c+2)
   c=c+3

##Translations of the original cDNA sequence
ProteinORF1=[]
for c in ORF1:                                  #Iter the nucleotic position in the ORF
    Codon=Seq[c]+Seq[c+1]+Seq[c+2]              #Select the three nucleotic of a codon in the sequence
    ProteinORF1.append(GeneticCode_1Letter[Codon])  #Translate this codon into an aminoacid residue and add it to the protein sequence

ProteinORF2=[]
for c in ORF2:
    Codon=Seq[c]+Seq[c+1]+Seq[c+2]
    ProteinORF2.append(GeneticCode_1Letter[Codon])

ProteinORF3=[]
for c in ORF3:
    Codon=Seq[c]+Seq[c+1]+Seq[c+2]
    ProteinORF3.append(GeneticCode_1Letter[Codon])

ProteinORF1=''.join(ProteinORF1)
ProteinORF2=''.join(ProteinORF2)
ProteinORF3=''.join(ProteinORF3)
print('\n\tThe aminoacid sequence in the ORF1 is:\n\t',ProteinORF1)
print('\n\tThe aminoacid sequence in the ORF2 is:\n\t',ProteinORF2)
print('\n\tThe aminoacid sequence in the ORF3 is:\n\t',ProteinORF3)


##Translations of the complementary sequence

###Reverse sequence
RevSeq=list(Seq)
RevSeq.reverse()
RevSeq=''.join(RevSeq)     
print('\n\nThe complementary sequence is:\n',RevSeq)

###Translations
ProteinRevORF1=[]
for c in ORF1:
    Codon=RevSeq[c]+RevSeq[c+1]+RevSeq[c+2]
    ProteinRevORF1.append(GeneticCode_1Letter[Codon])

ProteinRevORF2=[]
for c in ORF2:
    Codon=RevSeq[c]+RevSeq[c+1]+RevSeq[c+2]
    ProteinRevORF2.append(GeneticCode_1Letter[Codon])

ProteinRevORF3=[]
for c in ORF3:
    Codon=RevSeq[c]+RevSeq[c+1]+RevSeq[c+2]
    ProteinRevORF3.append(GeneticCode_1Letter[Codon])
    
ProteinRevORF1=''.join(ProteinRevORF1)
ProteinRevORF2=''.join(ProteinRevORF2)
ProteinRevORF3=''.join(ProteinRevORF3)
print('\n\tThe aminoacid sequence in the ORF1 is:\n\t',ProteinRevORF1)
print('\n\tThe aminoacid sequence in the ORF2 is:\n\t',ProteinRevORF2)
print('\n\tThe aminoacid sequence in the ORF3 is:\n\t',ProteinRevORF3)

print('\n\nNote to the user: The symbol * indicates a STOP codon')


#Save the output in a new file in format FASTA
ProteinFile=open('Protein_Sequences.txt','w')
ProteinFile.write('\n>Aminoacid sequence based in ORF1 of cDNA\n')
ProteinFile.write(ProteinORF1)
ProteinFile.write('\n\n>Aminoacid sequence based in ORF2 of cDNA\n')
ProteinFile.write(ProteinORF2)
ProteinFile.write('\n\n>Aminoacid sequence based in ORF3 of cDNA\n')
ProteinFile.write(ProteinORF3)
ProteinFile.write('\n\n>Aminoacid sequence based in ORF1 of reverse cDNA\n')
ProteinFile.write(ProteinRevORF1)
ProteinFile.write('\n\n>Aminoacid sequence based in ORF2 of reverse cDNA\n')
ProteinFile.write(ProteinRevORF2)
ProteinFile.write('\n\n>Aminoacid sequence based in ORF3 of reverse cDNA\n')
ProteinFile.write(ProteinRevORF3)
print('\n\nThe aminoacid sequences have been saved in a new file called Protein_Sequences.txt')

#Close the files
SeqFile.close()
GeneticCodeFile.close()
ProteinFile.close()
print('\nEnd of the program')
