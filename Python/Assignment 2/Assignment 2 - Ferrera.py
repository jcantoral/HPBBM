#Assignment 2 - Ferrera, Alberto

#Input sequence and found mistakes

print('\t----Welcome to the DNA analyser----')
Seq=input('\nType your DNA sequence and press enter: ').upper()

    #RNA
if 'U' in Seq:
    print('\nWARNING: The sequence is RNA, not DNA. The following statistics is for this DNA convertion')
    RNA_Nuc='U'
    DNA_Nuc='T'
    TransTable=Seq.maketrans(RNA_Nuc, DNA_Nuc)
    Seq=Seq.translate(TransTable)
    print(Seq)

    #Protein
AA='QWERYIPSDFHKLVNM'

for nuc in Seq:
    for aa in AA:
        if aa==nuc:
            Seq=input('\nWARNING: The sequence is proteic. Please, type a DNA sequence: ').upper()
            break         #It should check again the sequence


#Statistics
len_Seq=len(Seq)
print('\nYour sequence has',len_Seq,'bases')

    #Nucleotides
print('\n\t---Nucleotide composition of your sequence---')
Nuc=['A','C','G','T']
for c in Nuc:
    print('\n% of',c,': ',round(Seq.count(c)*100/len_Seq,2))

    #Dinucleotides
print('\n\t---Dinucleotide composition of your sequence---')
Dinuc=['AA','AC','AG','AT','CC','CG','CT','GG','GT','TT']
for c in Dinuc:
    print('\n% of',c,': ',round(Seq.count(c)*100/(len_Seq/2),2))   #How is the percentage calculated with dinucleotides?

#Restriction enzymes
print('\n\n\t---Restriction analysis---')
RSites=['GAATTC','GGATCC','AAGCTT','GCGGCCGC']
REnz=['EcoRI','BamHI','HindIII','NotI']
Dict_REnz=dict(zip(RSites,REnz))
for c in RSites:
    if c in Seq:
        print('\nThe restriction enzyme',Dict_REnz.get(c),'cuts your sequence',Seq.count(c),'time(s) in the position(s): ', end='')
        Set_sites=[]
        site=Seq.find(c)+1                   #+1 is to consider the first position as +1
        while site>0 and site<=len_Seq:
            Set_sites.append(site)          
            if site==Seq.find(c,site):
                break
            else:
                site=Seq.find(c,site)
            
        print(Set_sites)
        
print('\n--End of the program--')
