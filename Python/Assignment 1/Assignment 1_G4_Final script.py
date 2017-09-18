
#Assignment 1
#Final script
#g4_ Leticia Rodriguez, Jesus Cantoral and Alberto Ferrera

#Enzymes database
DB_Enz={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"}

#Input DNA
print("Type your DNA sequence and press enter:")
DNA_Seq=input()          #We write an empty input after a print command, so that the user input is in the next line.
print()                  #We include line breaks to make the output more aesthetical
                        

#InputEnzyme
print("Type your chosen restriction enzyme (you can choose among EcoRI, HindIII, NotI and BamHI):")
Enz=input()
print()
print()

#Composition of the DNA
DNA_Seq=DNA_Seq.upper()

   #Lenght
DNA_length=len(DNA_Seq)
    
    #A
nA=DNA_Seq.count('A')
pA=round(nA*100/DNA_length,2)

    #C
nC=DNA_Seq.count('C')
pC=round(nC*100/DNA_length,2)

    #G
nG=DNA_Seq.count('G')
pG=round(nG*100/DNA_length,2)

    #T
nT=DNA_Seq.count('T')
pT=round(nT*100/DNA_length,2)


print("   Nucleotide composition of your DNA sequence")
print("% of A:")
print(pA)
print()                                                
print("% of C:")
print(pC)
print()
print("% of G:")
print(pG)
print()
print("% of T:")
print(pT)
print()
print()


#Restriction enzyme target in the sequence
print('Is your sequence digested by the enzyme?')

q1=DB_Enz[Enz]in DNA_Seq
print(q1)
print()

#First cutting position
print('The first cutting position is located at the base:')
first=DNA_Seq.find(DB_Enz[Enz])
first=first+1       #To avoid confusion to the user, we will consider position 0 as +1, which makes more biological sense.
print(first)
print()
print("   Please note that the program considers the first nucleotide as 1")
print("   If the result is 0, it means that there is no target for your enzyme")
print()
print()
print("       Good digestion!")




