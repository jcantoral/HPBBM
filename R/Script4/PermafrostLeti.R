rm(list=ls())

#Reading all sequences.
Sequences <- sapply(list.files(), function (x) scan(x, what= character()))
stopCodons <- c("TAA", "TAG", "TGA")
termcodons <- grepl(paste(stopCodons, collapse = '|'),Sequences)

#For splitting sequences, if it has a prokariot termination codon, 
#it goes to prokariot group, the rest go to the other group.
prokariots <- Sequences[which(termcodons==TRUE)]
not.prokariots <- setdiff(Sequences, prokariots)

#For splitting sequences in individual characters.
prok.seqs <-(sapply(prokariots, function(x) unlist(strsplit(x,''))))
not.prok.seqs <-sapply(not.prokariots, function(x) unlist(strsplit(x,'')))

#Function that returns the sequence length.
stats1 <- function(x){
   l=length(x)
   return(l)
}
#Function that returns the frecuency of Ts of a sequence.
stats2 <-function(x){
  nTs <- sum(x=='T')
  freqTs <- nTs/length(x)
  return(freqTs)
}

#Summaries
summary(sapply(prok.seqs,stats1))
summary(sapply(prok.seqs,stats2))
summary(sapply(not.prok.seqs,stats1))
summary(sapply(not.prok.seqs,stats2))