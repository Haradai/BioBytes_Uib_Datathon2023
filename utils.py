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
