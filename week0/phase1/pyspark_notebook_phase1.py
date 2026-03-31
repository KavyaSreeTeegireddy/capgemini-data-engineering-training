from pyspark.sql import SparkSession
from pyspark.sql.functions import count
spark=SparkSession.builder.appName("Customer").getOrCreate()
customers = [
    (1, 'Ravi', 'Hyderabad', 25),
    (2, 'Sita', 'Chennai', 32),
    (3, 'Arun', 'Hyderabad', 28)
]
columns=["customer_id", "customer_name","city","age"]
df=spark.createDataFrame(data,columns)
df.show()

1) spark.sql("SELECT * FROM customers").show()

2) customers.filter(customers.city=='Chennai'").show()

3) spark.sql("SELECT * FROM customers WHERE age>25").show()

4) spark.sql("SELECT customer_name,city FROM customers").show()

5) spark.sql("SELECT city, COUNT(*) FROM customers GROUP BY city").show()
