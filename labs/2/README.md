# Using pyspark from python interpreter, RDD

* In this lab we use pyspark interactively on the local node
* We demonstrate how to use broadcast and shared variables, how to turn a text file or a list into RDD
* Start pyspark as follows:
  ```
  pyspark --master local[4]
  ```
* This brings you to python interpreter
* Inside the interpreter some pyspark modules are already loaded for you and Spark context is already set up:
  ```
  sc						  
  spark                                           
  lines = sc.textFile("README.md")                
  lines                                           
  lines.collect()                                 
  lines.count()	   				  
  l1 = lines.map(lambda line: len(line.split()))  
  l1                                              
  l2 = l1.reduce(lambda a,b: a if (a>b) else b)   
  l2
  pairs = lines.flatMap(lambda s: s.split()).map(lambda w: (w,1))
  pairs
  pairs.take(1)
  result = pairs.reduceByKey(lambda a,b: a+b)
  result
  print("\n".join(map(lambda x: "{} -> {}".format(*x), result.collect())))
  data = list(range(1000))
  distData = sc.parallelize(data)
  distData
  b = sc.broadcast(list(range(10)))
  b
  b.value
  a = sc.accumulator(0)
  a
  sc.parallelize(list(range(5))).foreach(lambda x: a.add(x))
  a.value
  ```
