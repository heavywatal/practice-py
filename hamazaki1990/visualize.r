library("tidyverse")
freq <- read_csv("~/github/practice-py/hamazaki1990/allelechangewf.csv")
freq
freqplot <- ggplot(freq, aes(x = generation, y = derived_allele_frequency))
freqplot <- freqplot + geom_line()
print(freqplot)

freq1 <- read_csv("~/github/practice-py/hamazaki1990/allelechangemo.csv")
freq1
freqplot1 <- ggplot(freq1, aes(x = generation, y = derived_allele_frequency))
freqplot1 <- freqplot1 + geom_path(size=2, linetype="dashed")
print(freqplot1)
