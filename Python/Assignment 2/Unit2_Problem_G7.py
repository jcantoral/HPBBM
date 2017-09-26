###Mi_grupo: g7(Francisco Ávila Pascual, Daniel Lillo Vergara, Víctor Mejías Pérez)
#   Functions added are meant to convert raw data into a string processable by python.
MySeq=input('\tIntroduce your DNA sequence:').upper().replace(' ','')
print('                            ')
print('                            ')
print('                            ')
print('                            ')

#   These list will be useful to narrow down the sequences which are neither DNA nor RNA.
Aminoacids_list=['D','E','F','H','I','K','L','M','N','P','Q','R','S','V','W','Y']
#   This list will be essencial for nucleotide and dinucleotide stadistics.
Nucleotides_list=['A','C','T','G']
#   'If' sentence will "translate" RNA to DNA, if necessary.
if 'U' in MySeq:
    print('\tThis is RNA, we procede to translate it to DNA...')
    print('\tStatistics will appear below')
    MySeq=MySeq.replace('U','T')
#   This loop will act as a proper filter for non-DNA/RNA sequences.
for letters in list(MySeq):
    if letters not in list(MySeq):
        print('warning  !!!  '*6)
        print('  !!!  warning'*6)
        print('                            ')
        print('\tTHIS IS NOT A NUCLEIC ACID SEQUENCE AND THIS PROGRAM CANNOT PROCESS IT.')
        print('                            ')
        print('warning  !!!  '*6)
        print('  !!!  warning'*6)
        exit()
    if letters in Aminoacids_list:
        print('warning  !!!  '*6)
        print('  !!!  warning'*6)
        print('                            ')
        print('\tTHIS IS NOT A NUCLEIC ACID SEQUENCE AND THIS PROGRAM CANNOT PROCESS IT.')
        print('                            ')
        print('warning  !!!  '*6)
        print('  !!!  warning'*6)
        exit()
        
print('                            ')
print('                            ')
print('                            ')
print('                            ')

print('\tSTATISTICS')
print('\t   Length:',len(MySeq))
#   'For' loop will provide us the percentage of each nucleotide
print('\tPercent of nucleotides:')
for nucleotide in Nucleotides_list:
    Percent_nucl=round((MySeq.count(nucleotide)/len(MySeq))*100,2)
    print('\t     %{}:'.format(nucleotide),Percent_nucl)
#   We declare an empty list which will be filled with the statistics obtained in next loop.
DiNucleotides_list=[]
#   This nested loop will provide us all the possible dinucleotides.
for nucl_1 in Nucleotides_list:
    for nucl_2 in Nucleotides_list:
        DiNucleotides=str(nucl_1)+str(nucl_2)
        DiNucleotides_list.append(DiNucleotides)
#   This 'for' loop will locate all dinucleotides in your DNA sequence
#   and provide us dinucleotide statistics.
print('\tPercent of dinucleotides:')
for dinucleotide in DiNucleotides_list:
    Percent_dinucl=round((MySeq.count(dinucleotide)/(len(MySeq)-1))*100,2)
    print('\t     %{}:'.format(dinucleotide),Percent_dinucl)
#   We define a non-fixed variable which is the position argument for .find() function.
print('\tRestriction enzymes:')
#   We declare a dictionary with the restriction enzymes names assigned to the restriction sites.
REnz_dict={'GAATTC':'EcoRI','GGATCC':'BamHI','AAGCTT':'HindIII','GCGGCCGC':'NotI'}
#   This nested complex loop will find all the restriction sites in your secuence
#   and inform the user about the position(s) of the restriction site(s).
for enzymes in REnz_dict:
#   Here we can see the use we gave to EndPos, the non-fixed variable mentioned above.
    if enzymes in MySeq:
        EndPos=0
        print('  \t',REnz_dict[enzymes],'cuts in position(s):')
        while EndPos>-1:
            EndPos=MySeq.find(enzymes,EndPos)
            if EndPos>-1:
                print('\t   ',EndPos+1)
                EndPos=EndPos+1
    if not(enzymes in MySeq):
        print('   \t',REnz_dict[enzymes], 'does not cut your sequence.')        
    


    
                
    
      
      
      

        
        
