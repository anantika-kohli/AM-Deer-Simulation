import os
import pandas as pd
import matplotlib.pyplot as plt


kp_values = [0, 0.25, 0.5, 0.75, 1]
mean_pheno_diff = []

for kp in kp_values:
    df = pd.read_csv(f"mate_pairs_P{kp}_with_pheno.csv")
    mean_pheno_diff.append(df["pheno_diff"].mean())

plt.figure(figsize=(7,5))
plt.plot(kp_values, mean_pheno_diff, marker="o")
plt.xlabel("Strength of assortative mating (k_p)")
plt.ylabel("Mean absolute phenotype difference between mates")
plt.title("Phenotype-based assortative mating")
plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()




kq_values = [0, 0.25, 0.5, 0.75, 1]
mean_q_diff = []

for kq in kq_values:
   
    df = pd.read_csv(f"mate_pairs_A{kq}_with_q_and_diff.csv")

   
    mean_q_diff.append(df["q_diff"].mean())

plt.figure(figsize=(7,5))
plt.plot(kq_values, mean_q_diff, marker="o")
plt.xlabel("Strength of assortative mating (k_q)")
plt.ylabel("Mean absolute ancestry difference between mates (|Δq|)")
plt.title("Ancestry-based assortative mating")
plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ecdf(x):
    x = np.sort(x)
    y = np.arange(1, len(x)+1) / len(x)
    return x, y

# random baseline
df_rand = pd.read_csv("C:\Users\Anantika\OneDrive - York University\Documents\Desktop\AM-Deer-Stimulation\IBD_random\mate_pairs_random_with_q_and_pheno_diff.csv)
x_r, y_r = ecdf(df_rand["pheno_diff"].dropna())

plt.figure(figsize=(7,5))
plt.plot(x_r, y_r, color="black", lw=2, label="Random mating")

# assortative mating curves
strengths = [0, 0.25, 0.5, 0.75, 1]
for s in strengths:
    df = pd.read_csv(f"mate_pairs_P{s}_with_pheno.csv")
    x, y = ecdf(df["pheno_diff"].dropna())
    plt.plot(x, y, label=f"AM = {s}")

plt.xlabel("|Δ phenotype between mates|")
plt.ylabel("Proportion of mate pairs")
plt.title("Mate phenotype similarity under random vs assortative mating")
plt.legend()
plt.tight_layout()
plt.show()

