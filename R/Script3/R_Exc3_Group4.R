#Group 4 -- R Exercise 3
#Jesus Cantoral, Alberto Ferrera, Leticia Rodriguez

rm(list=ls())
#Read data
leuk.dat <- read.table("leukemia.data.txt", row.names = 1)
leuk.dat.m <- data.matrix(leuk.dat)

leuk.class <- factor(scan("leukemia.class.txt", 
                          what = character()))
sex <- factor(rep(c("Male", "Female"), 
                  length.out = length(leuk.class)))

#======= 1. Tables and cross-tabs =======
table(sex)
table(sex, leuk.class)
xtabs(~ sex + leuk.class)
mytable <- xtabs(~ sex + leuk.class)
(as.data.frame(mytable))

#======= 2. Two subsetting operations =======
pvalues <- apply(leuk.dat.m, 1,
              function(x) t.test (x~leuk.class)$p.value)

mean(leuk.dat.m[which(pvalues < 0.01), 3])

median(leuk.dat.m[2, which(sex=="Male")])

#======= 3. Gene summaries by condition and sex =======
leuk.dat.t <- t(leuk.dat.m)
dim(leuk.dat.t)
leuk.dat.t[1:5, 1:6]

## 3.1
aggregate(leuk.dat.t[,c(1,2124,2600)],
          list(type = leuk.class), median)

## 3.2
aggregate(leuk.dat.t[,c(1,2124,2600)],
          list(type = leuk.class, sex = sex), median)


## 3.3
all.median <- aggregate(leuk.dat.t[,1:3051],
                        list(type = leuk.class, sex = sex), median)
all.median[1:4,1:10]
dim(all.median)


## 3.4
aggregate(leuk.dat.t[,c(1,2124,2600)],
          list(type = leuk.class, sex = sex),
          function(x) c(Mean = mean(x),
                        Median = median(x),
                        sd = sd(x)))

## 3.5
by(leuk.dat.t[,c(1,2124,2600)],
          list(type = leuk.class, sex = sex),
          summary)

aggregate(leuk.dat.t[,c(1,2124,2600)],
   list(type = leuk.class, sex = sex),
   summary)

##Check their classes
by.output <- by(leuk.dat.t[,c(1,2124,2600)],
   list(type = leuk.class, sex = sex),
   summary)

aggregate.output <- aggregate(leuk.dat.t[,c(1,2124,2600)],
          list(type = leuk.class, sex = sex),
          summary)
class(by.output)
class(aggregate.output)
