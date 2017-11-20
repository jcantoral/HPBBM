#Graphics assigment
#Ferrera

#1. The Data
#Read data
leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)

#Sex of the patients
leuk.class <- factor(scan("leukemia.class.txt", what = character()))
sex <- factor(rep(c("Male", "Female"), length.out = length(leuk.class)))

#2. The boxplot of PTEN and scatterplots with lots of info
#2.1 The boxplot
boxplot(leuk.dat.m[2124, ] ~ leuk.class,
        col = c("orange", "lightblue"),
        main = "Boxplots of PTEN by patient group",
        xlab = "Patient groups",
        ylab = "Gene expression (mRNA)")

#2.2 PTEN, HK-1, a third gene, patient status, and some sex
library(colorspace)
for.cex <- leuk.dat.m[2600, ] - min(leuk.dat.m[2600, ]) + 1 
the.cex <- 2 * for.cex/max(for.cex)

plot(leuk.dat.m[1,] ~ leuk.dat.m[2124, ],
     xlab = "PTEN",
     ylab = "HK-1",
     main = "HK-1 vs PTEN; symbol size proportional to gene 2600",
     pch = c(1, 2)[sex],
     col = diverge_hcl(2)[leuk.class],
     cex = the.cex
     )

abline(lm(leuk.dat.m[1,] ~ leuk.dat.m[2124, ]))

names.class <- rep(levels(leuk.class), rep (2,2))
names.sex <- rep(levels(sex), 2)
text.legend <- paste(names.class, names.sex, sep = ", ")
legend(-1.5, 1, legend = text.legend,
       col = diverge_hcl(2),
       pch = c(1, 2))


#3. Conditioning plots
##Coplot
coplot(leuk.dat.m[1,] ~ leuk.dat.m[2124,] | sex,
       xlab = "PTEN",
       ylab = "HK-1",
       panel = panel.smooth)

##Library lattice
library(lattice)

###smoothed fit
xyplot(leuk.dat.m[1,] ~ leuk.dat.m[2124,] | sex,
       xlab = "PTEN",
       ylab = "HK-1",
       panel = function(x, y) {
         panel.xyplot(x, y); panel.loess(x, y)})
###linear fit
xyplot(leuk.dat.m[1,] ~ leuk.dat.m[2124,] | sex,
       xlab = "PTEN",
       ylab = "HK-1",
       panel = function(x, y) {
         panel.xyplot(x, y); panel.lmline(x, y)})

##ggplot
library(ggplot2)

data.PHS <- data.frame(PTEN = leuk.dat.m[2124, ],
                  HK = leuk.dat.m[1, ],
                  Sex = sex)

ggplot(aes(x = PTEN, y = HK), data = data.PHS) + 
  geom_point() +
  geom_smooth(method = "lm") +
  geom_smooth(method = "loess") +
  facet_wrap( ~ Sex) +
  ylab("HK-1")


# 4. Histogram of p-values
p.v.t <- apply(leuk.dat.m, 1, 
               function (x) t.test(x ~ leuk.class)$p.value 
               )

hist(p.v.t, breaks = 50, freq = FALSE,
     xlab = "p-value",
     ylim =  c(0.3, 14),
     main = "P-values from t-test"
    )
box()
abline(h = 1, lty = 2)
axis(2, at = 1)

#FDR-adjusted p-values
sorted.p <- sort(p.v.t)
sorted.adj.p <- p.adjust(sorted.p, method = "fdr")

#Thresholds after finding the FDR
cut.05 <- sorted.p[names(sorted.adj.p[
                        length(which(sorted.adj.p <= 0.05))])]
cut.15 <- sorted.p[names(sorted.adj.p[
                        length(which(sorted.adj.p <= 0.15))])]

abline(v = c(cut.05, cut.15),
       col = c("red", "blue"),
       lty = c(4, 3)
       )
FDR1 <- paste("FDR <= 0.05. P <= ", round(cut.05, digits = 4))
FDR2 <- paste("FDR <= 0.15. P <= ", round(cut.15, digits = 4))
text.legend2 <- c(FDR1, FDR2)
legend(0.25, 10, legend = text.legend2,
       col = c("red", "blue"),
       lty = c(4, 3))


#5. Scatterplot of p-values
##compute p-values from a wilcoxon test
p.w.t <- apply(leuk.dat.m, 1, 
               function (x) wilcox.test(x ~ leuk.class)$p.value 
                )
##plot wilcoxon test vs t-test
plot(p.w.t ~ p.v.t,
     xlab = "p-values from t-test",
     ylab = "p-values from Wilcoxon",
     cex = 0.5)
abline(v = cut.15,
       col ="blue",
       lty = 3)
rug(p.v.t)
rug(p.w.t, side = 2)
