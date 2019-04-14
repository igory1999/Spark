# Using pyspark from jupyter notebook, DataFrames

* In this lab we use pyspark interactively on the local node again but from a jupyter notebook
* Also instead of RDD, we shall use DataFrame


1. You can run jupyter either on login node or better on compute node
2. If you are running on login node of midway 2, get the hostname into `h` variable as follows:
   ```
   h=`hostname -a`.rcc.uchicago.edu
   ```
3. If you are running on compute node of midway 2, first get to it with `sinteractive`:
   ```
   sinteractive -p broadwl --ntasks=8 --mem-per-cpu=2G --time=3:00:00
   ```
   If you want all CPU cores and all memory of the node, use instead
   ```
   sinteractive -p broadwl --exclusive --time=3:00:00
   ```
   To get host ip, run
   ```
   h=`hostname -i`
   ```
   instead of the above command.
4. Set the environment to load python and spark, if you have not done already so in the previous labs:
   ```
   source ../env.sh
   ```
   [Link](../env.sh) to the `env.sh`
5. Start jupyter web server as follows:
   ```
   PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS="notebook --no-browser --ip=$h" pyspark
   ```
6. Connect a browser running on your laptop to the URL printed by the previous command.
7. For more details how to run jupyter on midway compute nodes see [these instructions](https://git.rcc.uchicago.edu/ivy2/Jupyter_on_compute_nodes).
7. Open `lab3.ipynb`
8. Use `Ctrl+Enter` to execute a shell in jupyter notebook

