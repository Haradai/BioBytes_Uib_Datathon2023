import numpy as np
import pandas as pd

def process_chunk(chunk):
    df_rows = []
    indexed = []

    for row in chunk.iterrows():
        i, row = row
        for col in chunk.columns[3:]:  # Avoid A0
            t = col[3]
            specie = row["Scientific Name"]
            id = specie + "_" + col[0] + col[1] + "_" + col[4:]

            if id not in indexed:  # New row
                data_dict = {
                    "id": id,
                    "Specie": specie,
                    "System": col[0],
                    "Treatment": col[1],
                    "Replica": col[4:],
                }
                data_dict["t" + t] = row[col]
                df_rows.append(data_dict)
                indexed.append(id)
            else:  # Add
                idx = indexed.index(id)
                df_rows[idx]["t" + t] = row[col]

    return df_rows

def calculate_correlation_for_column(col, columns):
    # Load the dataset within each worker process
    dataset =  pd.read_csv("sample_by_specie_timewise.csv")
    dataset .fillna(0,inplace=True)

    col_idx = columns.index(col)
    col_corr = []

    for conditions, values, specie in tqdm(dataset,total=len(dataset)):
        filt_cond_byt = np.array(conditions)[:, col_idx]
        filt_cond_byt = filt_cond_byt.astype("float")

        corr = np.corrcoef(values, filt_cond_byt)
        col_corr.append(corr[1, 0])

    return col, col_corr