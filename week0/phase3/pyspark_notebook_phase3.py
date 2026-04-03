from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import sum, count

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales=spark.read.option("header", "true").csv("/samples/sales.csv")

#shows the customers table
customers.show()
#prints customer schema
customers.printSchema()
#identifies missing values
clean_customers = customers.dropna()
#cleans data
clean_customers = customers.fillna("Unknown")
#prints valid records
valid = customers.filter(
    col("customer_id").isNotNull() &
    col("first_name").isNotNull() &
    col("email").isNotNull()
)
titanic= spark.read.format("parquet").load("/samples/titanic.parquet")
titanic.show()
products= spark.read.format("json").load("/samples/products.json")"""


sales.show()
cleaned_data = sales.dropna(subset=["sale_date", "total_amount"])
cleaned_data= cleaned_data.withColumn("total_amount",col("total_amount").cast("int"))
daily_sales= clean.groupBy("sale_date").agg(sum("total_amount").alias("daily_sales")).orderBy("sale_date").show()


joined_data= customers.join(sales, "customer_id")
cleaned_data = joined_data.filter(
    col("city").isNotNull() & col("total_amount").isNotNull()
)
cleaned_data= cleaned_data.withColumn(
    "total_amount",col("total_amount").cast("int")
)
result= cleaned_data.groupBy("city").agg(sum("total_amount").alias("revenue")).show()

sales.groupBy("customer_id").agg(count("*").alias("order_count")).filter(col("order_count") > 2).show()



df = customers.join(sales, "customer_id")
df = df.withColumn("total_amount", col("total_amount").cast("int"))
result_df= df.groupBy("city", "customer_id").agg(sum("total_amount").alias("total_amount_spend"))result_df.show()


result_df = df.groupBy("customer_id", "city").agg(sum("total_amount").alias("total_amount_spend"),count("sale_id").alias("countof_order"))
result_df.show()
