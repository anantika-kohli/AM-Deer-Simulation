import os
import pandas as pd
import matplotlib.pyplot as plt

#Phenotype-based assortative mating

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
plt.subplots_adjust(left=0.15, right=0.95, top=0.88





#Ancestry-based assortative mating

kq_values = [0, 0.25, 0.5, 0.75, 1]
mean_q_diff = []

for kq in kq_values:
   
    df = pd.read_csv(f"5mate_pairs_A{kq}_with_q_and_diff.csv")

   
    mean_q_diff.append(df["q_diff"].mean())

plt.figure(figsize=(7,5))
plt.plot(kq_values, mean_q_diff, marker="o")
plt.xlabel("Strength of assortative mating (k_q)")
plt.ylabel("Mean absolute ancestry difference between mates (|Δq|)")
plt.title("Ancestry-based assortative mating")
plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()






#Chatgpt response for getting IBD file as random baseline (did not use though)
#RANDOM MATING

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# Helpers
# -----------------------
def ecdf(a):
    a = np.asarray(a)
    a = a[~np.isnan(a)]
    x = np.sort(a)
    y = np.arange(1, len(x) + 1) / len(x)
    return x, y

def mean_and_se(df, col):
    v = df[col].dropna().values
    m = np.mean(v)
    se = np.std(v, ddof=1) / np.sqrt(len(v)) if len(v) > 1 else np.nan
    return m, se

# -----------------------
# Paths + strengths
# -----------------------
strengths = [0, 0.25, 0.5, 0.75, 1]

# Edit these if your files live elsewhere
random_path = r"IBD_random/mate_pairs_random_with_q_and_pheno_diff.csv"

# If your ancestry-AM matepair outputs are named like: mate_pairs_A0_with_q_and_diff.csv, ..., mate_pairs_A1_with_q_and_diff.csv
ancestry_pattern = r"mate_pairs_A{S}_with_q_and_diff.csv"

# If your phenotype-AM matepair outputs are named like: mate_pairs_P0_with_pheno.csv, ..., mate_pairs_P1_with_pheno.csv
# (EDIT THIS to match your actual phenotype files)
pheno_pattern = r"mate_pairs_P{S}_with_pheno.csv"


# -----------------------
# Load RANDOM baseline
# -----------------------
rand = pd.read_csv(random_path)
rand_q_mean, rand_q_se = mean_and_se(rand, "q_diff")
rand_p_mean, rand_p_se = mean_and_se(rand, "pheno_diff")


# =========================================================
# PLOT 1: Mean |Δq| vs k_q (Ancestry-AM) + RANDOM baseline
# =========================================================
am_q_means = []
am_q_ses = []

for s in strengths:
    f = ancestry_pattern.format(S=s)
    df = pd.read_csv(f)
    m, se = mean_and_se(df, "q_diff")
    am_q_means.append(m)
    am_q_ses.append(se)

plt.figure(figsize=(7,4))
plt.plot(strengths, am_q_means, marker="o", label="Ancestry-based AM (varied k_q)")
plt.fill_between(strengths,
                 np.array(am_q_means) - np.array(am_q_ses),
                 np.array(am_q_means) + np.array(am_q_ses),
                 alpha=0.2)

plt.axhline(rand_q_mean, linestyle="--", label="Random mating baseline")
plt.axhspan(rand_q_mean - rand_q_se, rand_q_mean + rand_q_se, alpha=0.15)

plt.xlabel("Strength of assortative mating (k_q)")
plt.ylabel("Mean |Δ ancestry (q)| between mates")
plt.title("Random vs ancestry-based assortative mating")
plt.legend()
plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()


# =========================================================
# PLOT 2: Mean |Δ phenotype| vs k_p (Phenotype-AM) + RANDOM baseline
# =========================================================
# Only run this if you actually have phenotype-AM files matching pheno_pattern
try:
    am_p_means = []
    am_p_ses = []

    for s in strengths:
        f = pheno_pattern.format(S=s)
        df = pd.read_csv(f)
        m, se = mean_and_se(df, "pheno_diff")
        am_p_means.append(m)
        am_p_ses.append(se)

    plt.figure(figsize=(7,4))
    plt.plot(strengths, am_p_means, marker="o", label="Phenotype-based AM (varied k_p)")
    plt.fill_between(strengths,
                     np.array(am_p_means) - np.array(am_p_ses),
                     np.array(am_p_means) + np.array(am_p_ses),
                     alpha=0.2)

    plt.axhline(rand_p_mean, linestyle="--", label="Random mating baseline")
    plt.axhspan(rand_p_mean - rand_p_se, rand_p_mean + rand_p_se, alpha=0.15)

    plt.xlabel("Strength of assortative mating (k_p)")
    plt.ylabel("Mean |Δ phenotype| between mates")
    plt.title("Random vs phenotype-based assortative mating")
    plt.legend()
    plt.tight_layout()
    plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
    plt.show()
except FileNotFoundError:
    print("Phenotype-AM plot skipped: update pheno_pattern to match your phenotype mate-pair CSV filenames.")





#PLOT OF P AND A ONE ONE GRAPH FOR A SINGLE SIMULATION
import pandas as pd
import matplotlib.pyplot as plt

# Assortative mating strengths (must match your folder/file names)
assort_strength = [0, 0.25, 0.5, 0.75, 1]

# Vectors to store mean differences
ancestry_means = []
phenotype_means = []

# Build vectors from CSV files
for s in assort_strength:
    # ancestry
    dfA = pd.read_csv(f"5mate_pairs_A{s}_with_q_and_diff.csv")
    ancestry_means.append(dfA["q_diff"].mean())

    # phenotype
    dfP = pd.read_csv(f"5mate_pairs_P{s}_with_pheno.csv")
    phenotype_means.append(dfP["pheno_diff"].mean())


plt.figure(figsize=(8,5))

plt.plot(
    assort_strength,
    ancestry_means,
    marker="o",
    linewidth=2,
    color="tab:blue",
    label="Ancestry difference (mean |Δq|)"
)

plt.plot(
    assort_strength,
    phenotype_means,
    marker="s",
    linewidth=2,
    color="tab:orange",
    label="Phenotype difference (mean |Δ phenotype|)"
)

plt.xlabel("Assortative mating strength")
plt.ylabel("Mean absolute difference between mates")
plt.title("Ancestry and phenotype response to assortative mating")
plt.legend()
plt.grid(alpha=0.25)

# Optional: force y-scale if you want
plt.ylim(0, 0.6)

plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()






#ALL PLOTS FROM EACH SIMULATION ON ONE (what was used) - Basic code needs manual creation of the sim folders.

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = r"C:\Users\Anantika\OneDrive - York University\Documents\Desktop\AM-Deer-Stimulation"

sim_folders = ["sim1", "sim2", "sim3", "sim4", "sim5"]
k_vals = [0, 0.25, 0.5, 0.75, 1]

A_FILE = "{SIM}mate_pairs_A{K}_with_q_and_diff.csv" #made a folder A file for my ancestry output (mannual)
P_FILE = "{SIM}mate_pairs_kp_{K}_with_q.csv" #made a folder P flife for my phenotype output (mannual)

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"] #each for the 5 strengths

plt.figure(figsize=(9,5))

for sim, color in zip(sim_folders, colors):
    sim_num = sim[-1]   # sim1 -> "1", sim2 -> "2", etc.

    ancestry_means = []
    pheno_means = []

    for k in k_vals:
        a_path = os.path.join(BASE_DIR, sim, A_FILE.format(SIM=sim_num, K=k))
        p_path = os.path.join(BASE_DIR, sim, P_FILE.format(SIM=sim_num, K=k))

        dfA = pd.read_csv(a_path)
        dfP = pd.read_csv(p_path)

       # BOTH use q_diff now
        ancestry_means.append(dfA["q_diff"].dropna().mean())
        phenotype_means.append(dfP["q_diff"].dropna().mean())

    plt.plot(k_vals, ancestry_means, color=color, marker="o", linewidth=2,
             label=f"Ancestry ({sim})")

    plt.plot(k_vals, pheno_means, color=color, marker="s", linewidth=2, linestyle="--",
             label=f"Phenotype ({sim})")

plt.xlabel("Assortative mating strength")
plt.ylabel("Mean absolute ancestry difference between mates")
plt.title("Ancestry & phenotype vs assortative mating (sim1–sim5)")
plt.grid(alpha=0.25)
plt.legend(ncol=2, fontsize=9)
plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()









#ALL PLOTS FROM EACH SIMULATION ON ONE huge legend 
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = r"C:\Users\Anantika\OneDrive - York University\Documents\Desktop\AM-Deer-Stimulation"

sim_folders = ["sim1", "sim2", "sim3", "sim4", "sim5"]
k_vals = [0, 0.25, 0.5, 0.75, 1]


A_FILE = "{SIM}mate_pairs_A{K}_with_q_and_diff.csv"
P_FILE = "{SIM}mate_pairs_kp_{K}_with_q.csv"

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"]

plt.figure(figsize=(11,6)) 

for sim, color in zip(sim_folders, colors):
    sim_num = sim[-1]  # sim1 -> "1"

    ancestry_means = []
    phenotype_means = []

    for k in k_vals:
        k_str = f"{k:g}"  # KEY FIX: 1.0 -> "1", 0.50 -> "0.5"

        a_path = os.path.join(BASE_DIR, sim, A_FILE.format(SIM=sim_num, K=k_str))
        p_path = os.path.join(BASE_DIR, sim, P_FILE.format(SIM=sim_num, K=k_str))

        # read + take mean q_diff from BOTH
        if os.path.exists(a_path):
            dfA = pd.read_csv(a_path)
            ancestry_means.append(dfA["q_diff"].dropna().mean())
        else:
            print("[MISSING]", a_path)
            ancestry_means.append(np.nan)

        if os.path.exists(p_path):
            dfP = pd.read_csv(p_path)
            phenotype_means.append(dfP["q_diff"].dropna().mean())
        else:
            print("[MISSING]", p_path)
            phenotype_means.append(np.nan)

    plt.plot(k_vals, ancestry_means, color=color, marker="o", linewidth=2,
             label=f"Ancestry assortment ({sim})")

    plt.plot(k_vals, phenotype_means, color=color, marker="s", linewidth=2, linestyle="--",
             label=f"Phenotype assortment ({sim})")

plt.xlabel("Assortative mating strength")
plt.ylabel("Mean absolute ancestry difference between mates (mean |Δq|)")
plt.title("Mean mate-pair ancestry difference across simulations")
plt.grid(alpha=0.25)
plt.legend(ncol=2, fontsize=9)
plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
plt.show()




plt.figure(figsize=(11,6))  # bigger + wider

for sim, color in zip(sim_folders, colors):
    sim_num = sim[-1]

    ancestry_means = []
    phenotype_means = []

    for k in k_vals:
        k_str = f"{k:g}"

        dfA = pd.read_csv(os.path.join(BASE_DIR, sim,
                        f"{sim_num}mate_pairs_A{k_str}_with_q_and_diff.csv"))
        dfP = pd.read_csv(os.path.join(BASE_DIR, sim,
                        f"{sim_num}mate_pairs_kp_{k_str}_with_q.csv"))

        ancestry_means.append(dfA["q_diff"].mean())
        phenotype_means.append(dfP["q_diff"].mean())

    plt.plot(k_vals, ancestry_means, color=color, marker="o",
             label=f"A{sim_num}")   # ancestry
    plt.plot(k_vals, phenotype_means, color=color, marker="s",
             linestyle="--", label=f"P{sim_num}")  # phenotype

plt.xlabel("Assortative mating strength", fontsize=9)
plt.ylabel("Mean |Δq| between mates", fontsize=9)
plt.title("Mate-pair ancestry difference vs assortative mating", fontsize=10)

plt.grid(alpha=0.25)

# compact legend, outside plot
plt.legend(title="A = ancestry, P = phenotype",
           bbox_to_anchor=(1.02, 1),
           loc="upper left",
           fontsize=9)

plt.tight_layout()
plt.subplots_adjust(left=0.15, right=0.95, top=0.88, bottom=0.15)
from matplotlib.lines import Line2D

# custom legend entries (ONLY 2)
legend_elements = [
    Line2D([0], [0], color="black", lw=2, linestyle="-", label="Ancestry"),
    Line2D([0], [0], color="black", lw=2, linestyle="--", label="Phenotype")
]

plt.legend(
    handles=legend_elements,
    title="Assortment type",
    loc="center left",
    bbox_to_anchor=(1.05, 0.5),
    fontsize=10
)

plt.show()






#ALL PLOTS FROM EACH SIMULATION ON ONE legend fixed
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.figure(figsize=(12, 6))  # wider figure

for sim, color in zip(sim_folders, colors):
    sim_num = sim[-1]

    ancestry_means = []
    phenotype_means = []

    for k in k_vals:
        k_str = f"{k:g}"

        dfA = pd.read_csv(os.path.join(
            BASE_DIR, sim, f"{sim_num}mate_pairs_A{k_str}_with_q_and_diff.csv"
        ))
        dfP = pd.read_csv(os.path.join(
            BASE_DIR, sim, f"{sim_num}mate_pairs_kp_{k_str}_with_q.csv"
        ))

        ancestry_means.append(dfA["q_diff"].mean())
        phenotype_means.append(dfP["q_diff"].mean())

    # ancestry = solid
    plt.plot(k_vals, ancestry_means, color=color, marker="o", linewidth=2)

    # phenotype = dashed
    plt.plot(k_vals, phenotype_means, color=color, marker="s",
             linestyle="--", linewidth=2)

plt.xlabel("Assortative mating strength", fontsize=10)
plt.ylabel("Mean |Δq| between mates", fontsize=10)
plt.title("Mate-pair ancestry difference vs assortative mating", fontsize=11)
plt.grid(alpha=0.25)


legend_elements = [
    Line2D([0], [0], color="black", lw=2, linestyle="-", label="Ancestry"),
    Line2D([0], [0], color="black", lw=2, linestyle="--", label="Phenotype")
]

plt.legend(
    handles=legend_elements,
    title="Assortment type",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=10
)

plt.tight_layout(rect=[0, 0, 0.82, 1])  # reserve space for legend
plt.show()

