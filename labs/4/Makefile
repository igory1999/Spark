out:	
	mkdir -p output

sql:	out
	spark-submit --master local[3] --name 'SQL example' sql.py 1>sql.out 2>sql.err
rdd2df:	out
	spark-submit --master local[3] --name 'RDD 2 DF' rdd2df.py 1>rdd2df.out 2>rdd2df.err
files:	out
	rm -rf output/namesAndFavColors.parquet
	spark-submit --master local[1] --name 'files' files.py 1>files.out 2>files.err
hive: files out
	spark-submit --master local[1] --name 'hive' hive.py 1>hive.out 2>hive.err
sparksql: files out
	spark-sql --master local[1] --name "spark-sql example" -f hive.sql 1>spark_sql.out 2>spark_sql.err
clean:
	rm -r -f *~ *.out *.err *.log
cleanall: clean
	rm -rf output/* spark-warehouse metastore_db

