# R Exc4 (permafrost, stop codons et al.) - Jesus

# Remember to setwd() to the permafrost/ folder!
rm(list=ls())

genes <- sapply(list.files(),
                function(x) scan(x, what=""))

stopCodons <- c("TAA", "TAG", "TGA")

codon.search <- function(codons,seqs) {
    grep(paste(codons, collapse="|")
         , seqs
       , value = TRUE)
}
# grep understands the pipe symbol "|" as an OR operator

with.stop <- codon.search(stopCodons, genes)
without.stop <- setdiff(genes, with.stop)

summary(sapply(with.stop, nchar))
summary(sapply(without.stop, nchar))

T.content <- function(seq) {
    seq.Ts <- gsub("[^T]","",seq)
    return(sapply(seq.Ts, nchar)/ sapply(seq, nchar))
    }

summary(T.content(with.stop))
summary(T.content(without.stop))
