#HPBBM Python Assignment5 Jesus Draft
def AccNum(File): #Extracts the accession number from a RefSeq file
	import re
	AccNumFile=open(File,"r")
	for Line in AccNumFile:
		if (">" in Line):
			Seq=Line.strip()
	RE=r"[NX]M_.+\.."
	RegExp=re.compile(RE)
	ANum=RegExp.search(Seq)
	return(ANum.group())

def GeneticCode(): #Extracts genetic code using regexps
	import sys
	import re
	GCFile=open("GeneticCode_standard.csv","r")
	RECodons=r"[ACGT]{3}"
	REAA=r"\t.\t"
	RegExpCod=re.compile(RECodons)
	RegExpAA=re.compile(REAA)
	GCaa,GCcod=[],[]
	for Line in GCFile:
		GCaa.append(RegExpAA.search(Line).group().split("\t")[1])
		GCcod.append(RegExpCod.search(Line).group())
		#print(RegExpAA.search(Line).group().split("\t")[1])
		#print(RegExpCod.search(Line).group())
	GCDict=dict(zip(GCcod,GCaa))
	return(GCDict)
	GCFile.close()

def Main():

	from Assignment4_G4_Final import ReadFasta
	from Assignment4_G4_Final import ReverseComplement
	from Assignment4_G4_Final import Translation

	AN=AccNum(sys.argv[1])
	Seq=ReadFasta(sys.argv[1])
	RCompSeq=ReverseComplement(Seq)
	GC=GeneticCode()
	Translation(Seq,GC,AN+str(".fasta"))
	Translation(RCompSeq,GC,AN+str(".fasta"))
	print("Script has ended. Output file is",AN,".fasta")

if __name__=='__main__':
	import sys
	Main()


