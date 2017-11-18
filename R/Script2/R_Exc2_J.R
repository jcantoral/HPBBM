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

boxplot(leuk.dat.m["G2124",]~leuk.class, col= c("orange","lightblue"), 
        main= "a) Boxplot of PTEN by patient group",
        ylab= "Gene expression (mRNA)")

#2.2 PTEN, HK-1
library("colorspace")

for.cex <- leuk.dat.m["G1",] - min(leuk.dat.m["G1",])+1
the.cex <- 2* for.cex/max(for.cex)

plot(leuk.dat.m["G1",]~leuk.dat.m["G2124",], pch=c(21,24)[sex],
     col=diverge_hcl(2)[leuk.class], cex=for.cex,
     xlab="PTEN", ylab="HK-1", main="b) HK-1 vs PTEN; symbol size
     proportional to gene 2600")

lclass <- rep(levels(leuk.class), rep (2, 2))
lsex <- rep(levels(sex), 2)
text.legend <- paste(lclass, lsex, sep=", ")
legend(-1, y= 1 ,pch=c(21,24), legend = text.legend,
       col=diverge_hcl(2)[as.factor(lclass)])
abline(lm(leuk.dat.m["G1",]~leuk.dat.m["G2124",]), lty = 2)

#3 Conditioning plots:
#Figure 2
coplot(leuk.dat.m["G2600",]~leuk.dat.m["G2124",] | sex,
       panel= panel.smooth, xlab= "PTEN", ylab= "HK-1")

#Figure 3
library("lattice")
xyplot(leuk.dat.m["G2600",]~leuk.dat.m["G2124",] | sex,
       xlab= "PTEN", ylab= "HK-1",
       panel = function(x, y) {
         panel.xyplot(x, y)
         panel.loess(x, y) })

#Figure 4
xyplot(leuk.dat.m["G2600",]~leuk.dat.m["G2124",] | sex,
       xlab= "PTEN", ylab= "HK-1",
       panel = function(x, y) {
         panel.xyplot(x, y)
         panel.lmline(x, y) })

#Figure 5
library("ggplot2")
dgg <- data.frame(PTEN = leuk.dat.m[2124, ],
                        HK = leuk.dat.m[1, ],
                        Sex = sex)

fig5 <- (ggplot(dgg, aes(PTEN,HK)) 
           + geom_smooth(method="lm", se= FALSE, color="gray") +
           geom_point() + geom_smooth(method="loess") +
            facet_wrap(~Sex) + labs(y="HK-1"))
fig5 #To plot fig5

#4. The histogram of p.-values

p.v.t <- apply(leuk.dat.m, 1,
                  function(x) t.test (x~leuk.class)$p.value)


sorted.p <- sort (p.v.t)
sorted.adj.p <- p.adjust(sorted.p,
                         method = "fdr")

cut.05 <- p.v.t[names(sorted.adj.p[which(sorted.adj.p > 0.05)[1]-1])]
cut.15 <- p.v.t[names(sorted.adj.p[which(sorted.adj.p > 0.15)[1]-1])]

hist(p.v.t, breaks = 50, freq= FALSE,
     xlab = "p-value", main = "P-values from t-test") ; box()
axis(2, at=1)
abline(v=cut.05, col="red", lty = 3)
abline(v=cut.15, col="blue", lty = 4)
abline(h=1, lty=2, lwd=2)

legend(0.4, y=8, lty=c(3,4), col=c("red","blue"), 
       legend=c(paste("FDR <= 0.05. P <=", round(cut.05, 4)),
                legend=paste("FDR <= 0.05. P <=", round(cut.15, 4))))

#5 The scatterplot of p-values

w.v.t <- apply(leuk.dat.m, 1,
               function(x) wilcox.test (x~leuk.class)$p.value)

plot(w.v.t ~ p.v.t, rug= TRUE, cex=0.5,
     xlab="p-values from t-test", ylab= "p-values from Wilcoxon")
abline(v=cut.15, col="blue", lty = 4)
rug(w.v.t,side=2); rug(p.v.t, side = 1)         
