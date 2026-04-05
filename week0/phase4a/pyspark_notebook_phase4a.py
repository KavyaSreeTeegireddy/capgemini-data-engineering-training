# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, when
from pyspark.sql.window import Window
from pyspark.sql.functions import percent_rank

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales=spark.read.option("header", "true").csv("/samples/sales.csv")

sales_df = sales.withColumn("total_amount", col("total_amount").cast("int"))


# Gold,Silver,Bronze segmentation using conditional logic
segm_df = customers.join(sales_df, "customer_id").groupBy("first_name").agg(sum("total_amount").alias("total_amount_spend")).withColumn("segment",when(col("total_amount_spend") > 100, "Gold").when(col("total_amount_spend") >= 50, "Silver")
        .otherwise("Bronze")
    )
segm_df.show()

# Group data by segment and count customers
segm_df.groupBy("segment").agg(count("*").alias("countof_customers")).show()

# quantile-based segmentation
quantiles = segm_df.approxQuantile("total_amount_spend", [0.33, 0.66], 0)
q1, q2 = quantiles
quantile_df = segm_df.withColumn("segment_quantile",
    when(col("total_amount_spend") <= q1, "Low")
    .when(col("total_amount_spend") <= q2, "Medium")
    .otherwise("High")
)
quantile_df.show()

# Window-based Ranking
window = Window.orderBy("total_amount_spend")
rank_df = segm_df.withColumn("rank_percent", percent_rank().over(window))
compare_df = rank_df.withColumn("segment_rank",
    when(col("rank_pct") <= 0.33, "Low")
    .when(col("rank_pct") <= 0.66, "Medium")
    .otherwise("High"))

# Compare the results of different methods
compare_df.select(
    "first_name",
    "total_amount_spend",
    "segment",
    "segment_rank"
).show()