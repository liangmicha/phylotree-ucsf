#number of barcoded loci
#barcode length  ~10
#number of cell division from egg 50

#errors
#some varaiblility around barcode length sometimes 0. Normal with mean 6
#sequncing error rate?? [indel/mutation]
#possibility of rearrangement??? -> probably not
#eat up part of added barcoded and then add [AGTAGGG] => delete [TAGGG] => add [TTAAGTAGGG]

N=7
nucs = c ("A","C","G","T")
pdel = 0.05 #probability of a deletion of some nucs before adding new barcode
pmut = 0.05 #probability of a random point mutation somehwere in the barcode 

genBarcode <- function() {
 l = round(rnorm(1,6,4))
 if (l < 0) {
    l = 0
 }
 return(sample(1:4,l,replace=T))
}

# for (i in 1:10) {
# 	cat(genBarcode());
# }

parent = genBarcode()
pool = list()
pool[[1]] = parent
cat('\n')
cat('egg',nucs[pool[[1]]])
cat('\n')
numCycles = 3
for (cyc in 1:numCycles) {
	 pool2 = list()
	 cnt = 1
	 cat('cycle',cyc)
	 cat('\n')
	 for (c in 1:length(pool)) {
	     bc = pool[[c]]
	     #with probabiliyt p eat k chars of existing barcode, with probaiblyt p2 mutate some part of the barcode
	     cat('parent',c,nucs[pool[[c]]])
	     cat('\n')
	     N = length(bc)
	     s = 1
	     if (pdel > runif(1)) {
	     	s = round(min(N,runif(1,2,6)))
	     }
	     d1 =  c(genBarcode(),bc[s:N])
	     s = 1
	     if (pdel > runif(1)) {
	     	s = round(min(N,runif(1,2,6)))
	     }
	     d2 =  c(genBarcode(),bc[s:N])
	     pool2[[cnt]] = d1
     	     cat('daughter1',nucs[pool2[[cnt]]])
	     cat('\n')
	     cnt = cnt + 1
	     pool2[[cnt]] = d2
     	     cat('daughter2',nucs[pool2[[cnt]]])
	     cat('\n')
	     cnt = cnt + 1
	 }
	 cat('\n')
	 pool = pool2
}

cat('FINAL BARCODES','\n')
for (c in 1:length(pool)) {
    cat(c(c,nucs[pool[[c]][length(pool[[c]]):1]]))
    cat('\n')
}

#how many loci based on error rates and barcode lengths and read depth. will be missing some sequences low down on the tree. 

#visualize