# R script 1

## 1. Scripts
### 1.3

```
rm(list=ls())
x <- seq(from=123, to=297, by=3.5)
summary(x)
```

### 1.2
**1.2.1** Either copying the code or by opening <kbd>File>Open File (Ctrl+O)</kbd>,then selecting and running as <kbd>Ctrl+Enter</kbd>.<p>
**1.2.2** ```source("path/to/file.R", echo=TRUE)``` <p>
**1.2.3** ```$R --vanilla < path/to/file.R```

## 2. Some read.table operations

**2.1** ``` d1 <- read.table ("d1.txt", header = TRUE) ```
**2.2** ``` d2 <- read.table ("d2.txt", header = TRUE, na.strings= " ", sep= "\t") ```
**2.3** ``` d3 <- read.table ("d3.txt", header = FALSE, na.strings= " ", sep= "\t") ```
**2.4** ``` d4 <- read.table ("d4.txt", header = TRUE, comment.char="@") ```

## 3. Packages


