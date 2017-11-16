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

boxplot(leuk.dat.m["G2124",]~leuk.class,col=c("orange","lightblue"), 
        main="a) Boxplot of PTEN by patient group")

#2.2 PTEN, HK-1
require("colorspace")

for.cex <- leuk.dat.m["G2600",] - min(leuk.dat.m["G2600",])+1
the.cex <- 2* for.cex/max(for.cex)

plot(leuk.dat.m["G2600",]~leuk.dat.m["G2124",], pch=c(21,24)[sex],
     col=diverge_hcl(2)[leuk.class], cex=for.cex,
     xlab="PTEN", ylab="HK-1", main="b) HK-1 vs PTEN; symbol size
     proportional to gene 2600")

lclass <- rep(levels(leuk.class), rep (2, 2))
lsex <- rep(levels(sex), 2)
text.legend <- paste(lclass, lsex, sep=", ")
legend(1, y= 0 ,pch=c(21,24)[sex], legend = text.legend,
       col=diverge_hcl(2)[sex])
abline(lm(leuk.dat.m["G2600",]~leuk.dat.m["G2124",]))

?abline
