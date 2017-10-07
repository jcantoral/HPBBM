#Assignment 4 Jesus
def InputSeq(): #Parses sequence from user-defined file.
	import sys
	SeqFile=open(sys.argv[1],'r')
	Seq=""
	for Line in SeqFile:
		if not (">" in Line):
		   Seq=Seq+Line.strip()
	SeqFile.close()
	return(Seq)

def RevComp(Seq): #Returns the reverse complementary sequence
	Nucl="ACTG"
	CompNucl="TGAC"
	TransTable=str.maketrans(Nucl,CompNucl)
	NewSeq=Seq.translate(TransTable)
	return(NewSeq[::-1])

def GeneticCodeParser(GtcCode): #Parses a Genetic Code and returns a dictionary with its information
	GeneticCodeFile=open(GtcCode,"r")
	Triplets,TripletsList,AAoneletter=[],[],[]
	 
	for Line in GeneticCodeFile:
		Triplets=Line.split("\t")
		TripletsList.append(Triplets[0])
		AAoneletter.append(Triplets[1])
	GeneticCode=dict(zip(TripletsList,AAoneletter))
	GeneticCodeFile.close()
	return(GeneticCode)

def ProteinTranslator(DNASequence,GC,counter): #From a given sequence returns a protein sequence using a genetic code. The "counter" argument is handy to differentiate proteins in the output file.
	DNASequence=list(''.join(DNASequence))
	POut=""
	for Frame in range(3):
		Protein=""
		ProteinOutput=""
		for NucPos in range(Frame,(len(DNASequence)-2),3):
			Protein=Protein+(GC.get(DNASequence[NucPos]+DNASequence[NucPos+1]+DNASequence[NucPos+2]))
		ProteinOutput=("\n> Protein "+ str(counter)+ " Frame "+str(Frame)+"\n"+ProteinOutput+Protein)
		POut=POut+ProteinOutput
	return(POut)

def Main(): #Connects previous functions and exports information to the user-defined output file. A print() function informs the user the script has ended and the name of the output file.
	import sys
	Forward=str(InputSeq())
	Reverse=str(RevComp(Forward))
	Senses=[Forward,Reverse]
	GCs=["GeneticCode_standard.csv","GeneticCode_mito.csv"]
	OutputFile=open(sys.argv[2],"w")
	counter=1
	for Sense in Senses:
		for GC in GCs:
			OutputFile.write(ProteinTranslator(Sense,GeneticCodeParser(GC),counter))
			counter=counter+1
	print("Script has ended. Input file is",sys.argv[1],"and Output file is",sys.argv[2])
	OutputFile.close()

Main()
