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
    dfA$assortment_type <- "ancestry"
    dfA$simulation <- sim
    
    data_list[[counter]] <- dfA[, c("q_diff", "strengthAM", "assortment_type", "simulation")]
    counter <- counter + 1
    
    # phenotype assortment file
    fileP <- file.path(BASE_DIR, sim,
                       paste0(sim_num, "mate_pairs_kp_", k, "_with_q.csv"))
    
    dfP <- read.csv(fileP)
    dfP$strengthAM <- k
    dfP$assortment_type <- "phenotype"
    dfP$simulation <- sim
    
    data_list[[counter]] <- dfP[, c("q_diff", "strengthAM", "assortment_type", "simulation")]
    counter <- counter + 1
  }
}

data <- bind_rows(data_list)

data$assortment_type <- factor(data$assortment_type)
data$simulation <- factor(data$simulation)

head(data)
nrow(data)


model <- lm(q_diff ~ strengthAM * assortment_type, data = data)
summary(model)

install.packages(c("broom","knitr","kableExtra"))
library(broom)
library(knitr)
library(kableExtra)

table_model <- tidy(model)

table_model$term <- recode(table_model$term,
                           "(Intercept)" = "Intercept: random mating baseline (ancestry rule)",
                           "strengthAM" = "Slope: assortative mating strength under ancestry-based mating",
                           "assortment_typephenotype" = "Baseline shift: phenotype vs ancestry mating at strength = 0",
                           "strengthAM:assortment_typephenotype" = "Interaction: change in slope under phenotype-based mating")
kable(table_model,
      digits = 3,
      col.names = c("Term","Estimate","Std. Error","Statistic","p-value"),
      caption = "Linear model testing the effect of assortative mating strength and mating rule on ancestry difference between mates") |>
  kable_styling(full_width = FALSE)