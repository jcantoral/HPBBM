#Assignment 4 Modified to introduce the condition if __name__=='__main__'
#Group 4     Leticia Rodriguez, Jesus Cantoral and Alberto Ferrera

#Defining function for reading Fasta files
def ReadFasta(Name_of_File):
    Seq=""
    SeqFile=open(Name_of_File,"r")
    for Line in SeqFile:         
        if not (">" in Line): #In order to skip the first line.
                Seq=Seq+Line.strip()
    return(Seq)
    SeqFile.close()    

#Defining function for reading Genetic Codes
def ReadGeneticCode(Name_of_File):
    Codons=[]
    AA=[]
    MyCode=open(Name_of_File,"r")
    for Line in MyCode:          
        Line=Line.strip()
        GeneticCode=Line.split("\t")
        Codons.append(GeneticCode[0])
        AA.append(GeneticCode[1])
    Dictionary=dict(zip(Codons,AA)) #We are creating a dictionary in which the codons are the keys, and the aa are the values.
    return(Dictionary)
    MyCode.close()

#Defining function for generating the reverse complement
def ReverseComplement(Seq):
    Original_Symbols="ACTG"
    Complementaries="TGAC"
    TransTable=str.maketrans(Original_Symbols,Complementaries)
    NewSeq=Seq.translate(TransTable)
    Reverse_Complement=NewSeq[::-1]
    return(Reverse_Complement)

#Defining function for translating the sequence and printing in a different file.
def Translation(Seq,Code,File):
    Prot1=[]
    Prot2=[]
    Prot3=[]
    OutputFile=open(File,"a")

    for i in range(0,len(Seq)-2,3): #We are separating the Sequence in its codons, and the for each codon we are taking its value from the dictionary and adding it to a new list.
        Prot1.append(Code[Seq[i:i+3]])
        if i+3>=(len(Seq)):      
                break
        Prot2.append(Code[Seq[i+1:i+4]])
        if i+4>=(len(Seq)):
                 break              #With the breaks we avoid going on with translation if we have less than 3 bases.
        Prot3.append(Code[Seq[i+2:i+5]])
    OutputFile.write(">\n"+"".join(Prot1)+"\n"+">\n"+"".join(Prot2)+"\n"+">\n"+"".join(Prot3)+"\n")
    OutputFile.close()

#Main script
if __name__=='__main__':
    import sys
    Seq=ReadFasta(sys.argv[1]) #With sys.argv we are taking the name of the fasta file as an argument.
    StandardCode=ReadGeneticCode("GeneticCode_standard.csv")
    MitoCode=ReadGeneticCode("GeneticCode_mito.csv")
    rcSeq=ReverseComplement(Seq)
    Translation(Seq,StandardCode,sys.argv[2]) #With sys.argv we are taking the name of the future file as an argument.
    Translation(rcSeq,StandardCode,sys.argv[2])
    Translation(Seq,MitoCode,sys.argv[2])
    Translation(rcSeq,MitoCode,sys.argv[2])
    print('---End of script---')

