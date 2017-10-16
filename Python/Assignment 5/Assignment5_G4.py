#Assignment5
#Ferrera, Alberto

#Import the needed functions from script 4
from Assignment4_G4_FinalModificado import ReadFasta
from Assignment4_G4_FinalModificado import Translation
from Assignment4_G4_FinalModificado import ReverseComplement

#Define the needed functions
##This functions import the accession number of the sequence from the file
def Read_AN(FileName):
    File=open(FileName,'r')
    for Line in File:
            if '>' in Line:         #It looks for only in the first line (where the AN should be)
                Text=Line
    File.close()
    MyRE=r'[NX]M_\d{1,}\.\d'
    MyRegex=re.compile(MyRE)
    MyRes=MyRegex.search(Text)      #I used search instead findall because I just need one match and it is better to obtain it as a string.
    Accession_Number=MyRes.group()
    return(Accession_Number)

##This functions import the genetic code (with the one-letter code for the aas)
def Read_GenCode():
    Codons=[]
    AA=[]
    MyCode=open('GeneticCode_standard.csv',"r")
    for Line in MyCode:        
        MyRE=r'([ACTG]{3})\t([\w*])\t([A-Z][a-z]{2})\n'
        MyRegex=re.compile(MyRE)
        Result=MyRegex.search(Line)
        Codons.append(Result.groups()[0])
        AA.append(Result.groups()[1])
    Dictionary=dict(zip(Codons,AA))
    MyCode.close()
    return (Dictionary)
 
def Main():
    Seq=ReadFasta(sys.argv[1])
    Accession_Number=Read_AN(sys.argv[1])
    RevSeq=ReverseComplement(Seq)
    GenCode=Read_GenCode()
    Accession_Number+='.fasta'
    Translation(Seq,GenCode,Accession_Number)
    Translation(RevSeq,GenCode,Accession_Number)
    print('The result has been saved in a file named',Accession_Number)
 
if __name__=='__main__':
    import sys
    import re
    Main()
    print('\n---End of the script---')
    

