#The data
leuk.dat <- read.table('leukemia.data.txt', row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)
leuk.class <- factor(scan('leukemia.class.txt', what = ''))
sex <- factor(rep(c('Male', 'Female'), 19))
#Boxplot
boxplot(leuk.dat.m[2124,]~leuk.class, 
        col = c('orange', 'lightblue'), 
        main = 'a)Boxplot of PTEN by patient group')
#HK-1 vs PTEN, symbol size proportional to gene 2600
for.cex <- leuk.dat.m[2600,] - min(leuk.dat.m[2600,])+1
the.cex <- 2 * for.cex/max(for.cex)
p<-plot(leuk.dat.m[1,]~leuk.dat.m[2124,],
            xlab = 'PTEN', ylab = 'HK-1', 
            main = 'b)HK-1 vs.PTEN; symbol size proportional to gene 2600',
            pch = c(21, 24)[sex],
            cex = the.cex,
            col = diverge_hcl(2)[leuk.class])
lclass <- rep(levels(leuk.class), rep(2, 2))
lsex <- rep(levels(sex),2)
text.legend <- paste(lclass, lsex, sep = ', ')
legend(-1, 1, legend = text.legend,
       pch = c(21, 24)[factor(lsex)],
       col = diverge_hcl(2)[factor(lclass)])
abline(lm(leuk.dat.m[1,]~leuk.dat.m[2124,]), lty = 5)
#Conditional plots
coplot(leuk.dat.m[1,]~leuk.dat.m[2124,]|sex,
       panel = panel.smooth,
       xlab = 'PTEN', ylab = 'HK-1')

xyplot(leuk.dat.m[1,]~leuk.dat.m[2124,]|sex,
       xlab = 'PTEN', ylab = 'HK-1',
       panel = function(x, y) {
         panel.xyplot(x, y)
         panel.loess(x,y)
       })

xyplot(leuk.dat.m[1,]~leuk.dat.m[2124,]|sex,
       xlab = 'PTEN', ylab = 'HK-1',
       panel = function(x, y) {
         panel.xyplot(x, y)
         panel.lmline(x,y)
       })
#ggplot2
dgg <- data.frame(PTEN = leuk.dat.m[2124,],
                  HK = leuk.dat.m[1,],
                  Sex = sex)
ggplot(data = dgg, aes(PTEN, HK))+
  geom_smooth(method=loess) + 
  geom_point() + 
  facet_wrap(~Sex)+ labs(y='HK-1')
#Histogram of p-values
p.v.t <- apply(leuk.dat.m, 1, function(x) t.test(x~leuk.class)$p.value)
hist(p.v.t, freq=FALSE, breaks = 50,
     ylim=c(0.3, 14),
     xlab = 'p-value', ylab = 'Density')
abline(h=1, lty = 2)
axis(2, at = 1)
sorted.p <- sort(p.v.t)
sorted.adj.p <- p.adjust(sorted.p, method = 'fdr')
which(sorted.adj.p<0.05)
p.0.05 <- (which(sorted.adj.p<0.05))
cut.05 <- sorted.p [p.0.05[695]]
abline(v = cut.05, col = 'red', lty = 2)

p.0.15 <- (which(sorted.adj.p<0.15))
cut.15 <- sorted.p [p.0.15[1118]]
abline(v = cut.15, col = 'blue', lty = 2)
legend(0.4, 10, 
       legend = c(
         paste("FDR <= 0.05. P <=", round(cut.05, 4)),
         paste("FDR <= 0.15. P <= ", round(cut.15, 4))),
         col = c('red', 'blue'),
         lty = c(2, 2))
#Scatterplot of p-values
p.v.w <- apply(leuk.dat.m, 1, 
               function(x) wilcox.test(x~leuk.class)$p.value)
plot(p.v.w~p.v.t, xlab = 'p-values from t-test',
     ylab = 'p-values from Wilcoxon', cex = 0.5)
rug(p.v.t, side = 1)
rug(p.v.w, side = 2)
abline(v = cut.15, col = 'blue', lty = 2)