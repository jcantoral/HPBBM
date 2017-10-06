#Assignment 4
#Ferrera, Alberto

##Define functions
def ReadDNA(File):                      #Read the file and get the DNA sequence
    Seq=''
    DNAFile=open(File,'r')
    for Line in DNAFile:
        if not('>' in Line):
            Seq=Seq+Line.strip()
    DNAFile.close()
    return(Seq.upper())

def Reverse(Seq):                                   #Get the reverse complementary of the DNA sequence
    Rev_Dict={'A':'T','T':'A','G':'C','C':'G'}
    RevSeq=''
    for nucleotide in Seq:           
        RevSeq=Rev_Dict[nucleotide]+RevSeq
    return(RevSeq)

def Translate(Seq,Orientation):                             #Translate a sequence according to both genetic codes (Standard and mitochondrial)
    def ReadSt_Code():                                          ##Read the standard code
        Code=open('GeneticCode_standard.csv','r')
        St_Code={}
        for Line in Code:
            LineContent=Line.strip().split('\t')
            St_Code[LineContent[0]]=[LineContent[1:]]               ###Generate a dictionary with the standard code
        Code.close()
        return(St_Code)

    def ReadMito_Code():
        Code=open('GeneticCode_mito.csv','r')                   ##Read the mitochondrial code
        Mito_Code={}
        for Line in Code:
            LineContent=Line.strip().split()
            Mito_Code[LineContent[0]]=[LineContent[1:]]             ###Generate a dictionary with the mitochondrial code
        Code.close()
        return(Mito_Code)

    St_Code=ReadSt_Code()
    Mito_Code=ReadMito_Code()
    Codes=['Standard','Mitochondrial']
    ProteinSeq=''
    if Orientation=='+':
        ProteinFile.write('----Translations of your sequence---'+'\n')
    else:
        ProteinFile.write('----Translations of the reverse sequence---'+'\n')
    for Code in Codes:
        for Frame in range(0,3):
            ProteinFile.write('>Frame'+str(Frame+1)+' according to the '+Code+' genetic code '+'\n')
            for nuc in list(range(Frame, len(Seq),3)):
                if nuc <= (len(Seq)-3):
                    Codon=Seq[nuc:nuc+3]
                    if St_Code[Codon][0][0]=='*':
                        break
                    else:
                        ProteinSeq=ProteinSeq+St_Code[Codon][0][0]
            ProteinFile.write(ProteinSeq+'\n\n')
            
def Main(): 
    DNA=ReadDNA(sys.argv[1])            
    RevDNA=Reverse(DNA)
    Translate(DNA,'+')
    Translate(RevDNA,'-')
    
if __name__=='__main__':
    import sys
    ProteinFile=open(sys.argv[2],'w')
    Main()
    ProteinFile.close()
    print('\t---The results have been saved as',sys.argv[2],'---')
