#Leti's script
#Input sequence
Sequence=input("Type your DNA sequence and press enter:")
Seq=Sequence.upper()
Nitrogenous_Bases=["A","C","G","T","U"]
DNA_Bases=["A","C","G","T"]

#Checking for inputs different from DNA/RNA
counter=0
for n in Seq:
    if n not in Nitrogenous_Bases: #This way the program identifies any character that is not a nucleotide.
        counter=counter+1 #If there is a strange element in the sequence the counter will be different from 0 and the program will stop; otherwise, it will go on.

#Checking for RNA        
if counter==0:
    if "U" in Seq:
        Seq=Seq.replace("U","T") 
        print("This is RNA, not DNA. Your DNA sequence would be:",Seq) #It allows us to transform an RNA sequence into DNA.
    
    
#Statistics    
    print("\n---Sequence Statistics:")
    print("\n-Sequence length=",len(Seq),"bp")    
    print("\n-Nucleotides")
    for n in DNA_Bases:  #With the for loop we can go through all the DNA bases.
        pn=round(Seq.count(n)*100/len(Seq),2)
        out=("%"+n+":")
        print(out,pn)
    print("\n-Dinucleotides")
    for n in DNA_Bases:
        for k in DNA_Bases:   #With the for nested loop we can look for all the posible dinucleotide combiantions.
            dinucleotides=n+k
            pdn=round(Seq.count(n+k)*100/len(Seq),2)
            out=("%"+dinucleotides+":")
            print(out,pdn)
    
#Restriction enzymes dictionary
    print("\n---Restriction Enzymes")
    REnz={"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT","NotI":"GCGGCCGC"}
    for j in REnz:   #With the for loop we can check if there is any restriction enzyme target in the sequence.
        Cut= REnz[j] in Seq
        out="Does "+ j +" cut the sequence?"
        if Cut==1:
            print(out,"Yes!") #If there's a target, we go through a while loop.
            print("In which position/s?")
            a=0               #a acts as a counter
            while a<=len(Seq):
                hit=Seq.find(REnz[j],a,len(Seq)) #With "find" we look for the first time that the target appears in the sequence, counting from the position determined by the counter (which at the beginning will be 0, but then it will change) until the end of the sequence.
                if hit<0: #If hit is a negative number, it's because there are no more targets of that particular enzyme, so the program goes on to the next one.
                    break
                else:
                    print("+",hit+1)#To avoid confusion to the user, we will consider position 0 as +1, which makes more biological sense.
                    a=hit+1 #Each time the program finds a target, the counter takes the value of the target position + 1, which enables it to look for the next target.
               
        if Cut==0:
            print(out,"No =(")
            continue #With continue the program looks for the next restriction enzyme targets.
else:
    print("We regret to inform you that this program only runs with RNA and DNA sequences.")
print("\nEND OF SCRIPT")


