import random
port = random.randint(9000,10000)
host = 'localhost'

f = open("mync.sh", "w")
print("nc -lp {} -v -s {}".format(port, host), file = f)
f.close()

f = open("mystream.sh", "w")
print("spark-submit --master local[3] word_count.py {} {} 2>word_count.err".format(port, host), file = f)
f.close()

