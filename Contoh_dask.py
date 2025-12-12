import dask.dataframe as dd # type: ignore
df = dd.read_csv("data_5gb.csv")
# Operasi paralel
hasil = df.groupby("kategori").harga.mean().compute()
print(hasil)