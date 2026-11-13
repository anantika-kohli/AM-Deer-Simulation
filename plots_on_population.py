library(reticulate)
import pandas as pd
import matplotlib.pyplot as plt

assort_strength = [0, 0.25, 0.5, 0.75, 1]
variances = []

for a in assort_strength:
    df = pd.read_csv(f"IBD_kp_{a}/aggregated_results_primary.csv")

    # keep final generation only
    final_gen = df["generation"].max()
    df_final = df[df["generation"] == final_gen]

    # compute variance of phenotype
    var_pheno = df_final["phenotype_score"].var()
    variances.append(var_pheno)

# plot
plt.figure(figsize=(6,4))
plt.plot(assort_strength, variances, marker="o")
plt.xlabel("Assortative mating strength (kp)")
plt.ylabel("Phenotype variance")
plt.title("Phenotype variance increases with assortative mating")
plt.tight_layout()
plt.show()
