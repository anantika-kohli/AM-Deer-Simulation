library(dplyr)

# Main folder containing sim1 ... sim5
BASE_DIR <- "C:/Users/Anantika/OneDrive - York University/Documents/Desktop/AM-Deer-Stimulation"

# Simulation folders and assortative mating strengths
sim_folders <- c("sim1", "sim2", "sim3", "sim4", "sim5")
k_vals <- c(0, 0.25, 0.5, 0.75, 1)

# Empty list to store all dataframes
data_list <- list()
counter <- 1

# Loop through each simulation
for (sim in sim_folders) {
  
# Extract number from folder name: "sim1" -> "1"
  sim_num <- sub("sim", "", sim)
  
# Loop through each assortative mating strength
  for (k in k_vals) {
 
# Ancestry-based assortment file
 
    fileA <- file.path(
      BASE_DIR,
      sim,
      paste0(sim_num, "mate_pairs_A", k, "_with_q_and_diff.csv")
    )
    
    dfA <- read.csv(fileA)
    dfA$strengthAM <- k
    dfA$assortment_type <- "ancestry"
    dfA$simulation <- sim
    
    data_list[[counter]] <- dfA[, c("q_diff", "strengthAM", "assortment_type", "simulation")]
    counter <- counter + 1
    

# Phenotype-based assortment file
  
    fileP <- file.path(
      BASE_DIR,
      sim,
      paste0(sim_num, "mate_pairs_kp_", k, "_with_q.csv")
    )
    
    dfP <- read.csv(fileP)
    dfP$strengthAM <- k
    dfP$assortment_type <- "phenotype"
    dfP$simulation <- sim
    
    data_list[[counter]] <- dfP[, c("q_diff", "strengthAM", "assortment_type", "simulation")]
    counter <- counter + 1
  }
}

# Combine all files into one dataframe
data <- bind_rows(data_list)

# Make categorical variables factors
data$assortment_type <- factor(data$assortment_type, levels = c("ancestry", "phenotype"))
data$simulation <- factor(data$simulation)

# Create separate slope variables for each mating rule
data$AM_ancestry <- ifelse(data$assortment_type == "ancestry", data$strengthAM, 0)
data$AM_phenotype <- ifelse(data$assortment_type == "phenotype", data$strengthAM, 0)

# Quick checks
head(data)
nrow(data)
table(data$simulation)
table(data$assortment_type)
table(data$strengthAM)

# Fit linear model
model <- lm(q_diff ~ assortment_type + AM_ancestry + AM_phenotype, data = data)

# Show results
summary(model)