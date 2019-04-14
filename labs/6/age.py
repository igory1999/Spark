from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.functions import avg

spark = SparkSession.builder.getOrCreate()

userSchema = StructType().add("name", "string").add("age", "integer")
csvDF = spark \
    .readStream \
    .option("sep", ";") \
    .schema(userSchema) \
    .csv("input_csv")


averageAge = csvDF.select(avg(csvDF.age))

query = averageAge.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
