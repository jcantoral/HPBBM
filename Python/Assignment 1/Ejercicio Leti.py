#Leticia's script
#Input DNA sequence and restriction enzyme
DNA=input("Enter your DNA sequence:")
RE=input("Enter your restriction enzime (you can choose among EcoRI, HindIII, NotI and BamHI)")
#Composition of the DNA sequence
numberC=DNA.upper().count("C")
numberG=DNA.upper().count("G")
numberT=DNA.upper().count("T")
numberA=DNA.upper().count("A")
percentC=numberC/len(DNA)
percentG=numberG/len(DNA)
percentT=numberT/len(DNA)
percentA=numberA/len(DNA)
print("%C:")
print(percentC)
print("%G:")
print(percentG)
print("%T:")
print(percentT)
print("%A:")
print(percentA)
#Restriction enzymes dictionary
REnz={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"}
#Boolean function to check if the sequence has the restriction enzyme target
Cut=REnz[RE] in DNA.upper()
print("Would the restriction enzime digest your DNA sequence?")
#We only want to know the first cutting position IF there is at least one target in the sequence. Therefore we stablish the if conditionals
if Cut==1:
    print("Yes! =)")
    #FCP stands for first cutting position
    FCP=DNA.upper().find(REnz[RE])
    print("What would the first cutting position be?")
    print(FCP)
if Cut==0:
    print("No =(")
    

