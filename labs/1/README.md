# Line counting example

* In this lab we shall see how to run a simple line counting example in Spark on local machine and on the cluster, how to do the same thing with RDDs and DataFrames.  
* Set up an environment:
  ```
  source ../env.sh
  ```
* Run line counting example with RDD, on local machine, using 3 cores:
  ```
  make rdd
  ```
* Standard output is in `rdd.out`, standard error is in `rdd.err`.
* Run line counting example with DF, on local machine, using 4 cores:
  ```
  make df
  ```
* Standard output is in `df.out`, standard error is in `df.err`.
* To delete output files:
  ```
  make clean
  ```
