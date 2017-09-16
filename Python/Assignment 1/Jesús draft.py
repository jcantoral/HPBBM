#HPBBM Assignment 1 - Jesus Cantoral draft
#Firstly, the script requests the user to input the DNA sequence
DNAseq=input("Welcome, please type DNA sequence and hit enter: ")

#The script then determines the A/G/C/T % content, turning it to all uppercase (just in case) and counting each base (using a .count() funcion), then dividing by the length (using a len() function) of the "DNAseq" input chain and multiplying by 100, and rounding to two decimal points for simplicity.
print("\n -- Content of bases: --")
print(+round((DNAseq.upper().count("A"))/len(DNAseq)*100,2),"% A")
print(+round((DNAseq.upper().count("G"))/len(DNAseq)*100,2),"% G")
print(+round((DNAseq.upper().count("C"))/len(DNAseq)*100,2),"% C")
print(+round((DNAseq.upper().count("T"))/len(DNAseq)*100,2),"% T\n")

#The user is then asked for a Restriction Enzyme to cut with, among the ones included in the dictionary later defined in line 16. The answer is stored as a string.
REnzquery=input("Please type the enzyme to restrict with, you may choose between BamHI, EcoRI, HindIII or NotI: ")
print("\nIs there at least a target for", REnzquery, "in your DNA sequence?\n ")

REnz={"EcoRI":"GAATTC", "BamHI":"GGATCC", "HindIII":"AAGCTT", "NotI":"GCGGCCGC"}

#The following if/else conditions separate both possible cases: either there IS a restriction site and the script determines the position of the first site, OR there IS NOT a restriction site, which just informs the user.
#Thanks to the REnz dictionary and the RENzquery string, it is easy to determine if there is any restriction site inside the DNAseq string declared in line 3.
if (REnz[REnzquery] in DNAseq.upper())==True:
    print("Yes, there is. The first cutting site is in position", DNAseq.upper().find(REnz[REnzquery]),".\n")
else:
    print ("Oh, sorry. There is not a restriction site for", REnzquery,".\n")

#An informative print() function lets the user know the script has ended.
print("-----End of script-----")
