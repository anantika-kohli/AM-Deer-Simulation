library(dplyr)

BASE_DIR <- "C:/Users/Anantika/OneDrive - York University/Documents/Desktop/AM-Deer-Stimulation"

sim_folders <- c("sim1", "sim2", "sim3", "sim4", "sim5")
k_vals <- c(0, 0.25, 0.5, 0.75, 1)

data_list <- list()
counter <- 1

for (sim in sim_folders) {
  
  sim_num <- sub("sim", "", sim)
  
  for (k in k_vals) {
    
    # ancestry assortment file
    fileA <- file.path(BASE_DIR, sim,
                       paste0(sim_num, "mate_pairs_A", k, "_with_q_and_diff.csv"))
    
    dfA <- read.csv(fileA)
    dfA$strengthAM <- k
    dfA$type <- "ancestry"
    dfA$simulation <- sim
    
    data_list[[counter]] <- dfA[, c("q_diff", "strengthAM", "type", "simulation")]
    counter <- counter + 1
    
    # phenotype assortment file
    fileP <- file.path(BASE_DIR, sim,
                       paste0(sim_num, "mate_pairs_kp_", k, "_with_q.csv"))
    
    dfP <- read.csv(fileP)
    dfP$strengthAM <- k
    dfP$type <- "phenotype"
    dfP$simulation <- sim
    
    data_list[[counter]] <- dfP[, c("q_diff", "strengthAM", "type", "simulation")]
    counter <- counter + 1
  }
}

data <- bind_rows(data_list)

data$type <- factor(data$type)
data$simulation <- factor(data$simulation)

head(data)
nrow(data)