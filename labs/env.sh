module purge
module load Anaconda3/5.1.0
PYTHON=`which python`
export PYSPARK_PYTHON=$PYTHON
export PYSPARK_DRIVER_PYTHON=$PYTHON
module load spark/2.3.0

