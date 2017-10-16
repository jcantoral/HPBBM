from Assignment4_Leti import ReadFasta
from Assignment4_Leti import ReverseComplement
from Assignment4_Leti import Translation

def ReadRefSeq(Name_of_File):
    import re
    SeqFile=open(Name_of_File,"r")
    for Line in SeqFile:
        if ">" in Line:
            MyRE=r'[NX]M_\d+.\d'
            MyRegex=re.compile(MyRE)
            Result=MyRegex.search(Line)
            return(Result.group())
            break
    SeqFile.close()

def ReadGeneticCode(Name_of_File):
    import re
    Codons=[]
    AA=[]
    MyCode=open(Name_of_File,"r")
    for Line in MyCode:        
        MyRE=r'([ACTG]{3})\t([\w*])\t([A-Z][a-z]{2})\n'
        MyRegex=re.compile(MyRE)
        Result=MyRegex.search(Line)
        Codons.append(Result.groups()[0])
        AA.append(Result.groups()[1])
    Dictionary=dict(zip(Codons,AA))
    return Dictionary
    MyCode.close()

def Main():
    import re
    Seq=ReadFasta(sys.argv[1])
    RefSeq=str(ReadRefSeq(sys.argv[1]))
    Code=ReadGeneticCode("GeneticCode_standard.csv")
    rcSeq=ReverseComplement(Seq)
    OutputFile=open(RefSeq[0:]+ ".txt","a")
    OutputFile.write(">"+RefSeq+"\n")
    Translation(Seq,Code,OutputFile)
    Translation(rcSeq,Code,OutputFile)

if __name__=='__main__':
    import sys
    Main()
    
