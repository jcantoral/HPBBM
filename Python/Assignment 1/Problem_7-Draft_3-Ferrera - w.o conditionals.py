
#Problem 7
#Third Draft

#Alberto Ferrera

#Enzymes database
DB_Enz={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"}

#Input DNA
print("Type your DNA sequence and press enter:")
DNA_Seq=input()
print()

#InputEnzyme
print("Type your chosen restriction enzyme among the following:")
print(DB_Enz.keys())
                    #Note: I don't like this comand, but I don't know other way to show the enzymes stored in the database
Enz=input()
print()
print()

#Composition of the DNA
DNA_Seq=DNA_Seq.upper()

   #Lenght
DNA_length=len(DNA_Seq)
    
    #A
nA=DNA_Seq.count('A')
pA=nA/DNA_length    
pA*=100
pA=round(pA,2)

    #C
nC=DNA_Seq.count('C')
pC=nC/DNA_length
pC*=100
pC=round(pC,2)

    #G
nG=DNA_Seq.count('G')
pG=nG/DNA_length
pG*=100
pG=round(pG,2)

    #T
nT=DNA_Seq.count('T')
pT=nT/DNA_length
pT*=100
pT=round(pT,2)


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


#Is the sequence digested by the selected enzyme?
print('Is your sequence digested by the enzyme?')

q1=DB_Enz[Enz]in DNA_Seq
print(q1)
print()

#First cutting position
print('The first cutting position is located at the base*:')
first=DNA_Seq.find(DB_Enz[Enz])
first=first+1       #To avoid the initial 0 index
print(first)
print()
print("   * The program considers the first nucleotide as 1")
print("     If the result is 0, it means that there is no cutting position")
print()
print()
print("       Good digestion!")




