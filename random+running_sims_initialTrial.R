rm(list = ls())
gc()

source("Gene-Tinder (1).R")

# Assortative mating gradient
assort_strength <- c(0, 0.25, 0.50, 0.75, 1)

# Scale to biologically meaningful decay strengths
k_scaled <- assort_strength * 10
results_kq <- vector("list", length(assort_strength))

#scenario one ancestry
for (i in seq_along(assort_strength)) {
  
  results_kq[[i]] <- Gene_Tinder(
    experiment_name = paste0("IBD_A_kq_", assort_strength[i]),
    num_runs = 10,
    parallel = TRUE,
    
    num_generations = 5,
    initial_pop = 300,
    max_population_size = 300,
    
    pheno_loci_indices = 1:100,
    pheno_heritability = 0.3,
    species_A_ratio = 0.5,
    min_fitness_scalar = 0.5,  #ask what this parameter should be included for now and what scale to set
    
    weight_dist = 0.1,
    weight_q = 0.9,
    weight_p = 0,              # phenotype assortment OFF
    
    k_dist = 5.0,
    k_q = k_scaled[i],         # SCALED sweep
    k_p = 1                 # irrelevant here
  )
}

names(results_kq) <- paste0("kq_", assort_strength)
results_kp <- vector("list", length(assort_strength))

#Scenario two phenotype
for (i in seq_along(assort_strength)) {  
  
  results_kp[[i]] <- Gene_Tinder(
    experiment_name = paste0("IBD_P_kp_", assort_strength[i]),
    num_runs = 10,
    parallel = TRUE,
    
    num_generations = 5,
    initial_pop = 300,
    max_population_size = 300,
    
    pheno_loci_indices = 1:100,
    pheno_heritability = 0.3,
    species_A_ratio = 0.5,
    min_fitness_scalar = 0.5,
    
    weight_dist = 0.9,
    weight_q = 0,              # genetic assortment OFF
    weight_p = 0.1,
    
    k_dist = 10.0,
    k_q = 1,                 # irrelevant here
    k_p = k_scaled[i]          # SCALED sweep
  )
}

#Scenario 3 complete random mating

  results_kp[[i]] <- Gene_Tinder(
    experiment_name = "IBD_random",
    num_runs = 10,
    parallel = TRUE,
    
    num_generations = 5,
    initial_pop = 300,
    max_population_size = 300,
    
    pheno_loci_indices = 1:100,
    pheno_heritability = 0.3,
    species_A_ratio = 0.5,
    min_fitness_scalar = 0.5,
    
    weight_dist = 0.9,
    weight_q = 0,              # genetic assortment OFF
    weight_p = 0,
    
    k_dist = 10.0,
    k_q = 1.0,                 # irrelevant here
    k_p = 1.0         # SCALED sweep
  )

names(results_kp) <- paste0("kp_", assort_strength)
