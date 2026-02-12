import pandas as pd

#PHENO AT AM 0.5
import pandas as pd

df = pd.read_csv("run1IBD_P_kp_0.5/P0.5aggregated_results_primary.csv")

# offspring rows where both parents are known
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
    .sort_values(["run_id","generation","n_offspring"], ascending=[True, True, False])
)

# parents are from generation-1
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

parents = df[["run_id", "generation", "id", "q_score"]].copy()
parents["id"] = pd.to_numeric(parents["id"], errors="coerce")

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})

dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs match types
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")

# merge q onto mate pairs
mate_pairs = mate_pairs.merge(moms, on=["run_id","parent_generation","maternal_id"], how="left")
mate_pairs = mate_pairs.merge(dads, on=["run_id","parent_generation","paternal_id"], how="left")

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()

# absolute q difference
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

mate_pairs.to_csv("1mate_pairs_kp_0.5_with_q.csv", index=False)
print("Saved:", len(mate_pairs))





#PHENO AT AM 0.25
import pandas as pd

df = pd.read_csv("run1IBD_P_kp_0.25/P0.25aggregated_results_primary.csv")

# offspring rows where both parents are known
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
    .sort_values(["run_id","generation","n_offspring"], ascending=[True, True, False])
)

# parents are from generation-1
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

parents = df[["run_id", "generation", "id", "q_score"]].copy()
parents["id"] = pd.to_numeric(parents["id"], errors="coerce")

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})

dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs match types
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")

# merge q onto mate pairs
mate_pairs = mate_pairs.merge(moms, on=["run_id","parent_generation","maternal_id"], how="left")
mate_pairs = mate_pairs.merge(dads, on=["run_id","parent_generation","paternal_id"], how="left")

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()

# absolute q difference
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

mate_pairs.to_csv("1mate_pairs_kp_0.25_with_q.csv", index=False)
print("Saved:", len(mate_pairs))



#PHENO AT AM 0
import pandas as pd

df = pd.read_csv("run1IBD_P_kp_0/P0aggregated_results_primary.csv")

# offspring rows where both parents are known
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
    .sort_values(["run_id","generation","n_offspring"], ascending=[True, True, False])
)

# parents are from generation-1
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

parents = df[["run_id", "generation", "id", "q_score"]].copy()
parents["id"] = pd.to_numeric(parents["id"], errors="coerce")

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})

dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs match types
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")

# merge q onto mate pairs
mate_pairs = mate_pairs.merge(moms, on=["run_id","parent_generation","maternal_id"], how="left")
mate_pairs = mate_pairs.merge(dads, on=["run_id","parent_generation","paternal_id"], how="left")

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()

# absolute q difference
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

mate_pairs.to_csv("1mate_pairs_kp_0_with_q.csv", index=False)
print("Saved:", len(mate_pairs))



##PHENO AT AM 0.75
import pandas as pd

df = pd.read_csv("run1IBD_P_kp_0.75/P0.75aggregated_results_primary.csv")

# offspring rows where both parents are known
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
    .sort_values(["run_id","generation","n_offspring"], ascending=[True, True, False])
)

# parents are from generation-1
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

parents = df[["run_id", "generation", "id", "q_score"]].copy()
parents["id"] = pd.to_numeric(parents["id"], errors="coerce")

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})

dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs match types
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")

# merge q onto mate pairs
mate_pairs = mate_pairs.merge(moms, on=["run_id","parent_generation","maternal_id"], how="left")
mate_pairs = mate_pairs.merge(dads, on=["run_id","parent_generation","paternal_id"], how="left")

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()

# absolute q difference
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

mate_pairs.to_csv("1mate_pairs_kp_0.75_with_q.csv", index=False)
print("Saved:", len(mate_pairs))




##PHENO AT AM 1
import pandas as pd

df = pd.read_csv("run1IBD_P_kp_1/P1aggregated_results_primary.csv")

# offspring rows where both parents are known
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
    .sort_values(["run_id","generation","n_offspring"], ascending=[True, True, False])
)

# parents are from generation-1
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

parents = df[["run_id", "generation", "id", "q_score"]].copy()
parents["id"] = pd.to_numeric(parents["id"], errors="coerce")

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})

dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs match types
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")

# merge q onto mate pairs
mate_pairs = mate_pairs.merge(moms, on=["run_id","parent_generation","maternal_id"], how="left")
mate_pairs = mate_pairs.merge(dads, on=["run_id","parent_generation","paternal_id"], how="left")

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()

# absolute q difference
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

mate_pairs.to_csv("1mate_pairs_kp_1_with_q.csv", index=False)
print("Saved:", len(mate_pairs))



#ANCESTRY AT AM 0
import pandas as pd

df = pd.read_csv("run5IBD_A_kq_0\A0aggregated_results_primary.csv")
print(df.columns)

offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()
print("offspring rows:", len(offspring))

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
)

# FIX 1: parents are typically from generation - 1 (parents of gen g offspring are in gen g-1)
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

# parent lookup table
parents = df[["run_id", "generation", "id", "q_score"]].copy()

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})
dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs are numeric and match
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")
moms["maternal_id"] = pd.to_numeric(moms["maternal_id"], errors="coerce")
dads["paternal_id"] = pd.to_numeric(dads["paternal_id"], errors="coerce")

# merge using parent_generation (g-1), not offspring generation (g)
mate_pairs = mate_pairs.merge(
    moms,
    on=["run_id", "parent_generation", "maternal_id"],
    how="left"
)

mate_pairs = mate_pairs.merge(
    dads,
    on=["run_id", "parent_generation", "paternal_id"],
    how="left"
)

print("missing mom_q:", mate_pairs["mom_q"].isna().sum())
print("missing dad_q:", mate_pairs["dad_q"].isna().sum())

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

# optional: keep the columns tidy
mate_pairs = mate_pairs.drop(columns=["parent_generation"])

mate_pairs.to_csv("mate_pairs_A0_with_q_and_diff.csv", index=False)
print("Saved rows:", len(mate_pairs))




#ANCESTRY AT AM 0.25
import pandas as pd

df = pd.read_csv("run5IBD_A_kq_0.25\A0.25aggregated_results_primary.csv")
print(df.columns)

offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()
print("offspring rows:", len(offspring))

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
)

# FIX 1: parents are typically from generation - 1 (parents of gen g offspring are in gen g-1)
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

# parent lookup table
parents = df[["run_id", "generation", "id", "q_score"]].copy()

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})
dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs are numeric and match
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")
moms["maternal_id"] = pd.to_numeric(moms["maternal_id"], errors="coerce")
dads["paternal_id"] = pd.to_numeric(dads["paternal_id"], errors="coerce")

# merge using parent_generation (g-1), not offspring generation (g)
mate_pairs = mate_pairs.merge(
    moms,
    on=["run_id", "parent_generation", "maternal_id"],
    how="left"
)

mate_pairs = mate_pairs.merge(
    dads,
    on=["run_id", "parent_generation", "paternal_id"],
    how="left"
)

print("missing mom_q:", mate_pairs["mom_q"].isna().sum())
print("missing dad_q:", mate_pairs["dad_q"].isna().sum())

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

# optional: keep the columns tidy
mate_pairs = mate_pairs.drop(columns=["parent_generation"])

mate_pairs.to_csv("5mate_pairs_A0.25_with_q_and_diff.csv", index=False)
print("Saved rows:", len(mate_pairs))





#ANCESTRY AT AM 0.5
import pandas as pd

df = pd.read_csv("run5IBD_A_kq_0.5\A0.5aggregated_results_primary.csv")
print(df.columns)

offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()
print("offspring rows:", len(offspring))

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
)

# FIX 1: parents are typically from generation - 1 (parents of gen g offspring are in gen g-1)
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

# parent lookup table
parents = df[["run_id", "generation", "id", "q_score"]].copy()

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})
dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs are numeric and match
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")
moms["maternal_id"] = pd.to_numeric(moms["maternal_id"], errors="coerce")
dads["paternal_id"] = pd.to_numeric(dads["paternal_id"], errors="coerce")

# merge using parent_generation (g-1), not offspring generation (g)
mate_pairs = mate_pairs.merge(
    moms,
    on=["run_id", "parent_generation", "maternal_id"],
    how="left"
)

mate_pairs = mate_pairs.merge(
    dads,
    on=["run_id", "parent_generation", "paternal_id"],
    how="left"
)

print("missing mom_q:", mate_pairs["mom_q"].isna().sum())
print("missing dad_q:", mate_pairs["dad_q"].isna().sum())

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

# optional: keep the columns tidy
mate_pairs = mate_pairs.drop(columns=["parent_generation"])

mate_pairs.to_csv("5mate_pairs_A0.5_with_q_and_diff.csv", index=False)
print("Saved rows:", len(mate_pairs))





#ANCESTRY AT AM 0.75
import pandas as pd

df = pd.read_csv("run5IBD_A_kq_0.75\A0.75aggregated_results_primary.csv")
print(df.columns)

offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()
print("offspring rows:", len(offspring))

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
)

# FIX 1: parents are typically from generation - 1 (parents of gen g offspring are in gen g-1)
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

# parent lookup table
parents = df[["run_id", "generation", "id", "q_score"]].copy()

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})
dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs are numeric and match
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")
moms["maternal_id"] = pd.to_numeric(moms["maternal_id"], errors="coerce")
dads["paternal_id"] = pd.to_numeric(dads["paternal_id"], errors="coerce")

# merge using parent_generation (g-1), not offspring generation (g)
mate_pairs = mate_pairs.merge(
    moms,
    on=["run_id", "parent_generation", "maternal_id"],
    how="left"
)

mate_pairs = mate_pairs.merge(
    dads,
    on=["run_id", "parent_generation", "paternal_id"],
    how="left"
)

print("missing mom_q:", mate_pairs["mom_q"].isna().sum())
print("missing dad_q:", mate_pairs["dad_q"].isna().sum())

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

# optional: keep the columns tidy
mate_pairs = mate_pairs.drop(columns=["parent_generation"])

mate_pairs.to_csv("5mate_pairs_A0.75_with_q_and_diff.csv", index=False)
print("Saved rows:", len(mate_pairs))





#ANCESTRY AT AM 1

import pandas as pd

df = pd.read_csv("run5IBD_A_kq_1\A1aggregated_results_primary.csv"
)
print(df.columns)

offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()
print("offspring rows:", len(offspring))

mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"])
    .size()
    .reset_index(name="n_offspring")
)

# FIX 1: parents are typically from generation - 1 (parents of gen g offspring are in gen g-1)
mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

# parent lookup table
parents = df[["run_id", "generation", "id", "q_score"]].copy()

moms = parents.rename(columns={
    "generation": "parent_generation",
    "id": "maternal_id",
    "q_score": "mom_q"
})
dads = parents.rename(columns={
    "generation": "parent_generation",
    "id": "paternal_id",
    "q_score": "dad_q"
})

# make sure IDs are numeric and match
mate_pairs["maternal_id"] = pd.to_numeric(mate_pairs["maternal_id"], errors="coerce")
mate_pairs["paternal_id"] = pd.to_numeric(mate_pairs["paternal_id"], errors="coerce")
moms["maternal_id"] = pd.to_numeric(moms["maternal_id"], errors="coerce")
dads["paternal_id"] = pd.to_numeric(dads["paternal_id"], errors="coerce")

# merge using parent_generation (g-1), not offspring generation (g)
mate_pairs = mate_pairs.merge(
    moms,
    on=["run_id", "parent_generation", "maternal_id"],
    how="left"
)

mate_pairs = mate_pairs.merge(
    dads,
    on=["run_id", "parent_generation", "paternal_id"],
    how="left"
)

print("missing mom_q:", mate_pairs["mom_q"].isna().sum())
print("missing dad_q:", mate_pairs["dad_q"].isna().sum())

mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q"]).copy()
mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()

# optional: keep the columns tidy
mate_pairs = mate_pairs.drop(columns=["parent_generation"])

mate_pairs.to_csv("5mate_pairs_A1_with_q_and_diff.csv", index=False)
print("Saved rows:", len(mate_pairs))


 


#RANDOM MATING
df = pd.read_csv("IBD_random/Random_aggregated_results_primary.csv")
print(df.columns)

#remove all NA from the csv file
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()

#extract all offsprings with parents
print("offspring rows:", len(offspring))
offspring[["run_id","generation","maternal_id","paternal_id"]].head()
offspring = df.dropna(subset=["maternal_id", "paternal_id"]).copy()


mate_pairs = (
    offspring
    .groupby(["run_id", "generation", "maternal_id", "paternal_id"]) #Group rows that share the same values of these four columns
    .size() #number of offspring produced by that pair
    .reset_index(name="n_offspring") #Converts the grouped object into a normal DataFrame 
    .sort_values(["run_id","generation","n_offspring"], ascending=[True, True, False])
)

mate_pairs["parent_generation"] = mate_pairs["generation"] - 1

parents = df[["run_id", "generation", "id", "q_score", "phenotype_score"]].copy()

moms = parents.rename(columns={
    "id": "maternal_id",
    "q_score": "mom_q",
    "phenotype_score": "mom_pheno"
})

dads = parents.rename(columns={
    "id": "paternal_id",
    "q_score": "dad_q",
    "phenotype_score": "dad_pheno"
})


mate_pairs = mate_pairs.merge(
    moms,
    left_on=["run_id", "parent_generation", "maternal_id"],
    right_on=["run_id", "generation", "maternal_id"],
    how="left"
)

mate_pairs = mate_pairs.merge(
    dads,
    left_on=["run_id", "parent_generation", "paternal_id"],
    right_on=["run_id", "generation", "paternal_id"],
    how="left"
)


mate_pairs = mate_pairs.dropna(subset=["mom_q", "dad_q", "mom_pheno", "dad_pheno"]).copy()

mate_pairs["q_diff"] = (mate_pairs["mom_q"] - mate_pairs["dad_q"]).abs()
mate_pairs["pheno_diff"] = (mate_pairs["mom_pheno"] - mate_pairs["dad_pheno"]).abs()

mate_pairs.to_csv(
    "IBD_random/mate_pairs_random_with_q_and_pheno_diff.csv",
    index=False
)










