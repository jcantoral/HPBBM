# R Exc4 (permafrost, stop codons et al.) - Jesus

# Remember to setwd() to the permafrost/ folder!
rm(list=ls())

genes <- sapply(list.files(),
                function(x) scan(x, what=""))

#genes.lengths <- sapply(genes, nchar)

stopCodons <- c("TAA", "TAG", "TGA")

with.stop <- grep(paste(stopCodons, collapse="|")
                  , genes
                  , value = TRUE)
# grep understands the pipe symbol "|" as an OR operator

without.stop <- setdiff(genes, with.stop)

#----
#Some stats for my curiosity only
boxplot(sapply(with.stop, nchar)
        ,sapply(without.stop, nchar)
        )

summary(sapply(with.stop, nchar))
summary(sapply(without.stop, nchar))

#----

with.stop.Ts <-gsub("[^T]","",with.stop)
without.stop.Ts <- gsub("[^T]","",without.stop)

with.stop.Tcontent <- sapply(with.stop.Ts, nchar) / 
  sapply(with.stop, nchar)
without.stop.Tcontent <- sapply(without.stop.Ts, nchar) / 
  sapply(without.stop, nchar)

#boxplot(with.stop.Tcontent, without.stop.Tcontent)

summary(with.stop.Tcontent)
summary(without.stop.Tcontent)

# ----
# I just wanted to check the distribution of T content among
# all the sequences.

genes.Ts <-gsub("[^T]","",genes)
genes.Tcontent <- sapply(genes.Ts, nchar) / 
  sapply(genes, nchar)
plot(genes.lengths~genes.Tcontent)
summary(genes.Tcontent)
