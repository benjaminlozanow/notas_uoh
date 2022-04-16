import pandas as pd 

template = pd.read_excel("notas.xlsx")

master_df = template.drop(["Estado", "Nota", "Observaciones"], axis=1)
master_df.to_excel("master_notas.xlsx", index=False)

master_df["EVALUACION_NUMERO"] = pd.Series(dtype='float')
master_df.to_excel("molde_puntajes.xlsx", index=False)