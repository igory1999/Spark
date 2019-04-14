rdd:
	spark-submit --master local[3] --name 'Line counting with RDD' line_count_RDD.py README.md 1>rdd.out 2>rdd.err
df:
	spark-submit --master local[4] --name 'Line counting with DF'  line_count_DF.py  README.md 1>df.out  2>df.err

clean:
	rm -r -f *~ *.out *.err spark-warehouse
