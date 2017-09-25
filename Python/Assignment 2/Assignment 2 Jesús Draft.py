#HPBBM Assignment 2 - Jesus Cantoral draft
#Firstly, the scripts requests the user to input the DNA sequence
DNAinput=input("Welcome, please type sequence and hit enter: ").upper()

Aas=["R","N","D","Q","E","H","I","L","K","M","F","P","S","W","Y","V"] #Dictionary containing aminoacids other than A,C,G,T (which could equally be nucleotides).
AaCounter=0
for AaCheck in range(len(Aas)): #This for loop will search through DNAinput to check whether any aminoacids (from the Aas dictionary) are present.
        if (Aas[AaCheck] in DNAinput) == True:
                AaCounter=AaCounter+1 #If any aminoacids are found, this will increase the value of AaCounter. Any >0 would signify at least one type of Aa present in the sequence.

if AaCounter == 0: #(i.e. no aminoacids in sequence)
    
        if ("U" in DNAinput) and ("T" in DNAinput) == True: #The user could have introduced both Ts and Us so the script warns the user but carries on replacing Us into Ts.
            print ("Both Thymidine and Uracil found in your sequence, it seems either your sequence is wrong or the Nobel is near.\n The script will RT your Uracils into Thymidines, though.")
            
        elif ("U" in DNAinput) == True:
            print("Your sequence is RNA, it will be retrotranscribed into DNA and the script will proceed")

        DNAinput=DNAinput.replace("U","T") #The .replace() method will replace [as you would expect] Us for Ts.

        print("\n -- Sequence statistics: --") #Nearly identical to Assignment 1.
        print("Sequence:", DNAinput)
        print("Sequence length:",len(DNAinput),"bp.")
        for BaseCounter in range(4): #This avoids writing the same code for all four bases.
            Bases=["A","G","C","T"]
            print (round((DNAinput.count(Bases[BaseCounter]))/len(DNAinput)*100,2),"%",Bases[BaseCounter])


        REnzDict={"EcoRI":"GAATTC", "BamHI":"GGATCC", "HindIII":"AAGCTT", "NotI":"GCGGCCGC"} #Restriction Enzyme collection
        REnzList=["EcoRI","BamHI","HindIII","NotI"] #This list will connect functions that require a number with the Dictionary
        print("\n -- Restriction Enzyme Stats: --\n")
        for REnzCounter in range(len(REnzList)): #Sweep across all enzymes in RENzDict
                REsite=0 #This will determine the "scanning" position for the sequence so that the .find() method scans beyond the first cutting site.
                last=-2 #The preset value -2 is just a non -1 (inexisting sites) or >=0 (actually existing sites).
                while DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite) != last : #This loop will end when the last RE site is reached.                         
                    if DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite) == -1: #In case no sites were found
                            print("Sorry, there are no", REnzList[REnzCounter], "sites in the sequence")
                            break #And go to the next Enzyme
                    print("There is a cutting site for",REnzList[REnzCounter],"in position", DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite)) #In this case there is at least one restriction site.
                    last=DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite) #"last" will force the .find() method to keep on searching for another target
                    while (DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite)) == last:
                            REsite = DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite) +1 #Keep on searching: go to the next position (REsite determines the first nucleotide .find() will consider).
                    if DNAinput.find(REnzDict[REnzList[REnzCounter]],REsite) == -1: #This condition will occur when no more restriction sites are found, hence the loop must end.
                            break   
else: #In case any aminoacids are found
        print("Sorry, only DNA or RNA sequences are supported. The script will now halt.")

print("\n-----End of script-----")
