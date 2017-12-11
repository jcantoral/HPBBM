# R Exercise 4 (Permafrost) Group 4
# Jesus Cantoral, Alberto Ferrera, Leticia Rodriguez

# Please note this script works if the working directory
# is set to the "/permafrost" folder.

rm(list=ls()) #for a clean start

genes <- sapply(list.files(),
                function(x) scan(x, what=""))

stopCodons <- c("TAA", "TAG", "TGA")

codon.search <- function(codons,seqs) {
    grep(paste(codons, collapse="|") #for grep, the pipe is an OR operator
         , seqs
       , value = TRUE)
}

with.stop <- codon.search(stopCodons, genes)
without.stop <- setdiff(genes, with.stop)

summary( sapply( with.stop, nchar))
summary( sapply( without.stop, nchar))

T.content <- function(seq) {
    seq.Ts <- gsub( "[^T]", "", seq)
    return( sapply(seq.Ts, nchar) / sapply(seq, nchar))
    }

summary(T.content(with.stop))
summary(T.content(without.stop))
