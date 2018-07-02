require(knitr) # loads the required packages
source("TAutoCorrCode.R") # runs the code for TAutoCorr
knit2pdf("TAutoCorr_Analysis.Rnw") # Builds the LaTex analysis file containing data from TAutoCorr
file.rename(from = "TAutoCorr_Analysis.pdf", to = "../Results/TAutoCorr_Analysis.pdf") # Moves analysis to results folder
unlink("figure", recursive = TRUE) # remove unwanted files
unlink("TAutoCorr_Analysis.aux")
unlink("TAutoCorr_Analysis.log")