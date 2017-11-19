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
mytable <- as.data.frame(xtabs (~sex + leuk.class))

#Section 2: Two subsetting operations
pval <- apply(leuk.dat.m, 1,
              function(x) t.test (x~leuk.class)$p.value)

#Mean of expression of genes whose p-values < 0.01
## for patient 3:
mean(leuk.dat.m[which (pval<0.01), 3])

#Median of gene 2 expression in males:
median(leuk.dat.m[2,which(sex=="Male")])

#Section 3: Gene summaries by condition and sex

leuk.dat.t <- t(leuk.dat.m)
dim(leuk.dat.m);dim(leuk.dat.t) #To see how dimensions have changed
leuk.dat.t[1:5, 1:6]

#3.1 aggregate: The median of three genes by condition
aggregate(leuk.dat.t [,c(1,2124,2600)] ~ leuk.class, FUN = median)

#3.2 aggregate: The median of three genes by condition and sex
aggregate(x = leuk.dat.t [,c(1,2124,2600)],
          by = list (type = leuk.class, sex = sex),
          FUN=median)

#3.3 aggregate: The median of all the genes by condition and sex
all.median <- aggregate( x = leuk.dat.t,
                         by = list (type = leuk.class, sex = sex),
                         FUN = median)
all.median[,c(1:10)]
dim(all.median)

#3.4 aggregate: The mean and standard deviations of three genes by condition
##and sex
aggregate(x=leuk.dat.t [,c(1,2124,2600)],
          by = list (type = leuk.class, sex = sex), 
          function(x) c(mean=mean(x),sd=sd(x)))

#3.5 by and aggregate: those three genes again, but now use “summary”
by (data = leuk.dat.t [,c(1,2124,2600)],
    INDICES = list (type = leuk.class, sex = sex),
    FUN = summary ) #Argument names are not required, but informative.

aggregate(x=leuk.dat.t [,c(1,2124,2600)],
          by = list (type = leuk.class, sex = sex), 
          function(x) summary(x))
