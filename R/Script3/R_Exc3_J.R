#R Exc3 Jesus
rm(list=ls()) #Clean workspace

leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)
leuk.class <- factor(scan("leukemia.class.txt", what=""))
sex <- factor(c(rep(c("Male","Female"),19)))

#Section 1: Tables and cross-tabs

table(sex)
table(sex,leuk.class)

xtabs(~sex+leuk.class)
mytable <- as.data.frame(xtabs(~sex+leuk.class))

#Section 2: Two subsetting operations
pval <- apply(leuk.dat.m, 1,
              function(x) t.test (x~leuk.class)$p.value)

#Mean of expression of genes whose p-values < 0.01
## for patient 3:
mean(leuk.dat.m[which(pval<0.01),3])

#Median of gene 2 expression in males:
median(leuk.dat.m[2,which(sex=="Male")])

#Section 3: Gene summaries by condition and sex

leuk.dat.t <- t(leuk.dat.m)
dim(leuk.dat.m);dim(leuk.dat.t) #To see how dimensions have changed
leuk.dat.t[1:5, 1:6]
