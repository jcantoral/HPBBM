#R Exc2 Jesus
rm(list=ls()) #Clean workspace
#Remember to setwd() !!!

#Section 1: The data

leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)
leuk.class <- factor(scan("leukemia.class.txt", what=""))
sex <- factor(c(rep(c("Male","Female"),19)))

#Section 2: PTEN Boxplot/scatterplots
#2.1 Boxplot:

boxplot(leuk.dat.m["G2124",]~leuk.class,col=c("orange","lightblue"), main="a) Boxplot of PTEN by patient group")

