library("tidyverse")
setwd("~/github/practice-py/hamazaki1990/")
freq_wf <- read_csv("allelefreqwf.csv") %>%
    dplyr::mutate(model = "wf")
freq_wf
freq_mo <- read_csv("allelefreqmo.csv") %>%
    dplyr::mutate(model = "moran")
freq_mo
freq <- dplyr::bind_rows(freq_wf, freq_mo)
print(freq)
freqplot <- ggplot(freq, aes(x=generation, y=derived_allele_frequency, group=model, color=model))
freqplot <-freqplot + geom_line()
print(freqplot)
