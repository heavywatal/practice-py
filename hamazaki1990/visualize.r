library("tidyverse")
setwd("~/github/practice-py/hamazaki1990/")
freq_wf <- read_csv("allelefreqwf.csv") %>%
  dplyr::arrange(locus, step)
freq_wf
plotwf <- ggplot(freq_wf, aes(x=step, y=frequency, group=locus))
plotwf <-plotwf +geom_line()
plotwf <- plotwf + ylim(0, 1)
print(plotwf)
freq_mo <- read_csv("allelefreqmo.csv") %>%
  dplyr::arrange(locus, step)
freq_mo
plotmo <- ggplot(freq_mo, aes(x=step, y=frequency, group=locus))
plotmo <-plotmo +geom_line()
plotmo <- plotmo + ylim(0, 1)
print(plotmo)
