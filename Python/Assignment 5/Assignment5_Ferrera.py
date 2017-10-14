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
    GCode_File=open('GeneticCode_standard.csv','r')
    GCode_Content=''.join(GCode_File.readlines())       #It converts all the file in one string, so the regular expressions can be used in it.
    Codon_RE='[AGTC]{3}'
    OneLetter_RE='\t[\w\*]\t'
    Codon_Regex=re.compile(Codon_RE)
    OneLetter_Regex=re.compile(OneLetter_RE)
    Codons=Codon_Regex.findall(GCode_Content)               #It puts all the codons in one list
    OneLetterCode=OneLetter_Regex.findall(GCode_Content)
    AAs_Name=[]
    for AA in OneLetterCode:                                #It deletes the \t around the aa letter and create a list with all of them
        AAs_Name+=AA[1]
    Code_Dict=dict(zip(Codons,AAs_Name))                    #It creates the dictionary zipping the codons with the one-letter aa
    return(Code_Dict)

def Main():
    Seq=ReadFasta(sys.argv[1])
    Accession_Number=Read_AN(sys.argv[1])
    RevSeq=ReverseComplement(Seq)
    GenCode=Read_GenCode()
    Accession_Number+='.txt'
    Translation(Seq,GenCode,Accession_Number)
    Translation(RevSeq,GenCode,Accession_Number)
    print('The result has been saved in a file named',Accession_Number)
 
if __name__=='__main__':
    import sys
    import re
    Main()
    print('\n---End of the script---')
    
