#sap xep chen
sort1 <- function(x) {
  n <- length(x)
  for (i in 2:n) {
    temp <- x[i]
    j = i-1
    while ((x[i] > temp)&&(j>0)) {
      x[j+1] = x[j]
      j = j-1
    } 
    x[j+1] = temp
  }
  return(x)
}
dulieu <- c(5, 2, 4, 6, 1, 3)
sort1(dulieu)
