install.packages("tidyverse")
library("tidyverse")
allelefreq=read_csv("~/github/practice-py/hamazaki1990/allelechangewf.csv", col_names = FALSE)
names(allelefreq)=c("generation","derived_allele_frequency")
freqprot=ggplot(allelefreq, x=generation, y=derived_allele_frequency)
freqprot=freqprot+geom_line()
print(freqprot)
