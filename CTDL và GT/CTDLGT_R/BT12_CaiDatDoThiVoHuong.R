# DO THI

install.packages('igraph')
library(igraph)

# Vo Huong
help(graph)
vo_huong <- make_graph( ~ A-B-C-D-A, E-A:B:C:D, directed = FALSE)
plot(vo_huong)