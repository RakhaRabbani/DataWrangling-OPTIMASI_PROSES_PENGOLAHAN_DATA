from pyspark.sql import SparkSession

# Membuat session
spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()

# Membaca file CSV
df = spark.read.csv("log_transaksi.csv", header=True)

# Operasi paralel di cluster (filter dan agregasi)
hasil = df.groupBy("tipe_transaksi").count()

# Menampilkan hasil
hasil.show()