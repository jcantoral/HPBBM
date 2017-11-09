# R script 1
## 1. Scripts
### 1.1
```
rm(list=ls())
x <- seq(from=123, to=297, by=3.5)
summary(x)
```
### 1.2
**1.2.1** Either copying the code or by opening <kbd>File > Open File (Ctrl+O)</kbd>,then selecting and running as <kbd>Ctrl + Enter</kbd><p>
**1.2.2** ```source("path/to/file.R", echo=TRUE)``` <p>
**1.2.3** ```$R --vanilla < path/to/file.R``` <p>
## 2. Some read.table operations
**2.1** ```d1 <- read.table ("d1.txt", header = TRUE)``` <p>
**2.2** ```d2 <- read.table ("d2.txt", header = TRUE, na.strings= " ", sep= "\t")``` <p>
**2.3** ```d3 <- read.table ("d3.txt", header = FALSE, na.strings= " ", sep= "\t") ``` <p>
**2.4** ```d4 <- read.table ("d4.txt", header = TRUE, comment.char="@") ``` <p>
## 3. Packages
**3.1** Running a ```sessionInfo()``` command specifies versions of all packages that are installed. Up-to-date version is 2.4.0.<p>
**3.2** Same as 3.1. <p>
**3.3** The user first needs to "require" the package, running ```require(OncoSimulR)```, then ```OncoSimulR::oncoSimulIndiv()```
## 4. The Help
**4.1** A message ```character(0)``` appears. <p>
**4.2** A message suggesting the function ```car::scatter3d``` appears. <p>
**4.3** The message ```character(0)``` is replaced for ```"scatter3d"```. <p>
**4.4** According to the help, ``apropos()`` returns a vector including the names of all objects matching the query. I guess ``apropos`` needs the object to actually exist, and ``scatter3d`` only exists after requiring the ``car`` package. On the contrary, ``help.search`` returns the help information for the result of a search function. ``search``looks through all packages, not only those that have been loaded. <p>
**4.5** See answer **4.4**. <p>
**4.6** Definitely ``help.search`` is better. ``apropos`` would miss any package that is installed but not loaded in the session. <p>
**4.7** ``help.search("",package=NULL)``<p>
## 5. Saving objects
**5.1** 
```
x <- 97
y <- 95
save(x, file="oneObject.RData")
unlink("oneObject.RData")
unlink(".RData")
```
**5.2** ``save.image()`` saves the current workspace.<p>

## 6. Vectors, data frames, etc
**6.1** ``age <- c(rep(11,3),rep(63,2),rep(40,4),47)``<p>
**6.2** ``hr[age<45]`` <p>
**6.3** ``hr2 <- c(hr[age==63], hr[age==47],"Juan","Ana","Carmen")`` <p>
**6.4** ``matrix(hr2,ncol=2)[(which(hrm[,2]=="Juan/Ana")),1]`` <p>
**6.5** 
```
hr3 <- matrix(c(hr[age==63], hr[age==47],63,63,47),ncol=2)
rownames(hr3)<-c("Juan","Ana","Carmen")
``` 
**6.6**  ``data.fame(hr3)`` <p>
*No way this is how we're expected to do it. Let me rethink it…* <p>
**6.7** ``hr4 <- matrix(c("Juan", "Ana", "Carmen", hr[age==63], hr[age==47],63,63,47),ncol=3)`` <p>
**6.8** ``hr3["Juan",1]``<p>
**6.9** ``hr3["Juan",]``<p>
**6.10** ``hr4["Ana","X1"]``<p>
**6.11** 
```
hr5<-data.frame(hr4)
hr5[which(hr5=="Ana"),"X2"]
```
<!--This shows a terrible output.-->
**6.12**  ``hr5[which(hr5=="Ana"),]``<p>
**6.13** *I'm stuck here…* <p>
**6.14** *…not to mention here.* <p>
**6.15** ``matrix(c(hr[age>15],age[age>15]),ncol=2)``<p>
**6.16** No, they are not. There is an extra element at the end.<p>
**6.17** Correction (last element deleted): <p>
```
sex <- c("M", "F")[c(1, 2, 1, 1, 2, 2, 1, 1, 2, 2,)]
matrix(c(hr,age,sex),ncol=3
```

*And… I'm missing something here.*

## 7. Sort and order
*I need to figure* ***6.13*** *and* ***6.14***  *out before I can do this.*
