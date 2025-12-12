<div align="center">
  <h1>OPTIMASI PROSES PENGOLAHAN DATA</h1>
</div>
<div align="center">
  <h3><i>Transform Data, Unlock Insights, Drive Innovation</i></h3>
  <img src="https://img.shields.io/github/last-commit/RakhaRabbani/DataWrangling-AGREGASI_DAN_TRANSFORMASI_STRUKTURAL?style=flat-square&color=blue" alt="Last Commit">
  <img src="https://img.shields.io/github/languages/top/RakhaRabbani/DataWrangling-AGREGASI_DAN_TRANSFORMASI_STRUKTURAL?style=flat-square&color=blue" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/RakhaRabbani/DataWrangling-AGREGASI_DAN_TRANSFORMASI_STRUKTURAL?style=flat-square&color=blue" alt="Language Count">
  <br><br>
</div>

---

Repository ini berisi kumpulan contoh skrip Python untuk mempelajari berbagai teknologi pemrosesan data skala besar, meliputi:

* **PySpark** – pemrosesan terdistribusi berbasis cluster
* **Dask** – parallel computing untuk skala besar
* **Multiprocessing** – paralelisasi CPU-bound di mesin lokal
* **Google BigQuery** – query data warehouse kolumnar Google
* **AWS Athena** – query S3 dengan engine Presto/Trino

Setiap contoh menunjukkan cara melakukan pemrosesan paralel, query analitik, atau optimasi runtime pada dataset besar.

---

# **Prasyarat & Instalasi**

### **Versi Python**

Direkomendasikan: **Python 3.9+**

### **Library yang Dibutuhkan**

Install sesuai kebutuhan:

```bash
pip install pyspark
pip install dask[complete]
pip install google-cloud-bigquery
pip install boto3
```

---

# **Cara Menjalankan**

```bash
python Contoh_Spark_20GB_Partisi.py
python Contoh_dask.py
python Python_multiprocessing.py
python GoogleBigQuery_Python.py
python Athena.py
```

---

# **PySpark – Pemrosesan Paralel Cluster**

**File:** `Contoh_Spark_20GB_Partisi.py`

---

## **Tujuan**

Menunjukkan cara melakukan pemrosesan paralel pada dataset besar menggunakan Spark, dimulai dari membaca file CSV, melakukan operasi groupBy, dan menampilkan hasilnya.

---

## **Isi Utama Skrip**

* Membuat SparkSession
* Membaca file CSV berskala besar
* Melakukan operasi paralel di cluster
* Mengelompokkan data (`groupBy`)
* Menampilkan hasil analitik

---

## **Potongan Kode Penting**

```python
spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()

df = spark.read.csv("log_transaksi.csv", header=True)

hasil = df.groupBy("tipe_transaksi").count()

hasil.show()
```

---

## **Konsep yang Dipelajari**

* Eksekusi terdistribusi Spark
* Lazy evaluation
* Transformations & Actions
* Pembacaan file besar secara paralel

---

# **Dask – Parallel Processing untuk DataFrame Besar**

**File:** `Contoh_dask.py`

---

## **Tujuan**

Menunjukkan bagaimana Dask digunakan untuk memproses file CSV berukuran besar (hingga gigabyte) secara paralel di banyak worker.

---

## **Isi Utama Skrip**

* Memuat DataFrame menggunakan `dask.dataframe.read_csv`
* Melakukan agregasi paralel
* Menggunakan `.compute()` untuk mengeksekusi graph

---

## **Potongan Kode Penting**

```python
df = dd.read_csv("data_5gb.csv")
hasil = df.groupby("kategori").harga.mean().compute()
print(hasil)
```

---

## **Konsep yang Dipelajari**

* Task graph execution
* Lazy evaluation sama seperti Spark
* Pemrosesan data besar tanpa memenuhi RAM

---

# **Multiprocessing – Paralelisasi CPU Lokal**

**File:** `Python_multiprocessing.py`


---

## **Tujuan**

Menunjukkan penggunaan multiprocessing untuk mempercepat proses komputasi CPU-heavy menggunakan banyak core.

---

## **Isi Utama Skrip**

* Mendefinisikan fungsi komputasi `hitung()`
* Paralelisasi menggunakan `Pool()`
* Menjalankan perhitungan untuk range besar (1 juta angka)

---

## **Potongan Kode Penting**

```python
def hitung(n):
    return n * n * n

with Pool() as p:
    hasil = p.map(hitung, range(1_000_000))
```

---

## **Konsep yang Dipelajari**

* Multi-core CPU parallelism
* Perbedaan dengan threading (multiprocessing cocok untuk CPU-bound)
* Map-reduce sederhana


---

# **Google BigQuery – Cloud Data Warehouse Query**

**File Python:** `GoogleBigQuery_Python.py`
**File SQL:** `GoogleBigQuery_SQL.sql`


---

## **Tujuan**

Menunjukkan cara menjalankan query analitik BigQuery menggunakan Python Client dan SQL langsung.

---

## **Isi Utama Skrip**

* Inisialisasi client BigQuery
* Menjalankan query SQL
* Membaca hasil row-by-row
* Query menghitung transaksi per tanggal

---

## **Potongan Kode Penting (Python)**

```python
client = bigquery.Client(project="my-gcp-project")

query = """
    SELECT DATE(transaction_timestamp) AS dt, COUNT(*) AS total_tx
    FROM `myproject.mydataset.transactions`
    WHERE transaction_timestamp >= '2025-01-01'
    GROUP BY dt
"""

job = client.query(query)

for row in job:
    print(row.dt, row.total_tx)
```

---

## **Potongan Kode Penting (SQL)**

```sql
SELECT
    DATE(transaction_timestamp) AS dt,
    COUNT(*) AS total_tx,
    SUM(amount) AS total_amount
FROM `project.dataset.transactions`
WHERE transaction_timestamp >= '2025-01-01'
GROUP BY dt
ORDER BY dt;
```

---

## **Konsep yang Dipelajari**

* Query kolumnar storage
* Serverless data warehouse
* Pemrosesan PB-scale oleh BigQuery engine
* Integrasi SQL ↔ Python API



---

# **AWS Athena – Query Data di S3**

**File Python:** `Athena.py`
**File SQL:** `Athena.sql`

---

## **Tujuan**

Menunjukkan cara mengeksekusi query Athena (Presto/Trino) terhadap dataset di S3, dengan monitoring status job secara manual.

---

## **Isi Utama Skrip**

* Inisialisasi client boto3
* Submit query Athena
* Polling status eksekusi
* Mengambil hasil query jika sukses

---

## **Potongan Kode Penting**

```python
resp = client.start_query_execution(
    QueryString=query,
    QueryExecutionContext={'Database': DATABASE},
    ResultConfiguration={'OutputLocation': OUTPUT_LOCATION}
)

qid = resp['QueryExecutionId']
```

Polling:

```python
status = client.get_query_execution(QueryExecutionId=qid)['QueryExecution']['Status']['State']
```

---

## **Potongan SQL Athena**

```sql
SELECT 
    date_trunc('day', transaction_timestamp) AS dt,
    count(*) AS total_tx,
    sum(amount) AS total_amount
FROM "analytics_db"."transactions_parquet"
WHERE transaction_timestamp >= TIMESTAMP '2025-01-01'
GROUP BY dt
ORDER BY dt;
```

---

## **Konsep yang Dipelajari**

* Query lakehouse
* Integrasi Athena + S3
* Presto SQL
* Monitoring job Athena

---

# **Kesimpulan**

5 teknologi dalam repository ini mewakili pemrosesan data modern:

| Teknologi           | Jenis Pemrosesan             | Skala               |
| ------------------- | ---------------------------- | ------------------- |
| **PySpark**         | Cluster distributed compute  | Terabyte–Petabyte   |
| **Dask**            | Parallel compute skala besar | Gigabyte–Terabyte   |
| **Multiprocessing** | CPU parallel local           | Core CPU lokal      |
| **BigQuery**        | Cloud Data Warehouse         | Skalabilitas tinggi |
| **Athena**          | Query lake-based             | Data di S3          |
