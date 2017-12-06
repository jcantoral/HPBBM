#Assignment Permafrost
#Ferrera, Alberto 

rm(list = ls())

#Read the files
names.files <- sort(dir(path = "permafrost/", 
                        full.names = TRUE)[1:5000])

all.the.seq <- lapply(names.files, function(x)
                       scan(x, what = ""))

names(all.the.seq) <- lapply (names.files, function(x)
                    strsplit(x, "permafrost/")[[1]][2])

#Length and Frequency of Ts
seq.lengths <- as.numeric(lapply(all.the.seq, function(x)
                      nchar(x)))
names(seq.lengths) <- names(all.the.seq)

library(stringr)
total.Ts <- as.numeric(lapply(all.the.seq, function(x)
                    str_count(x, pattern = "T")))
freq.Ts <- total.Ts/seq.lengths
names(freq.Ts) <- names(all.the.seq)

#Separate sequences
stopCodons <- c("TAA", "TAG", "TGA")

codons.in.all <- grepl(paste(stopCodons, collapse="|"), all.the.seq)
seq.w.codons <- all.the.seq[which(codons.in.all)]
seq.wo.codons <- all.the.seq[which(codons.in.all == FALSE)]

#Summary
#Sequences with stop codons
summary(seq.lengths[names(seq.w.codons)])
summary(freq.Ts[names(seq.w.codons)])

#Sequences without stop codons
summary(seq.lengths[names(seq.wo.codons)])
summary(freq.Ts[names(seq.wo.codons)])






