LogisticRegression:	
	spark-submit --master local[3] --name 'Logistic Regression example' LogisticRegression.py 1>LogisticRegression.out 2>LogisticRegression.err
perceptron:	
	spark-submit --master local[3] --name 'Multilayer perceptron example' perceptron.py 1>perceptron.out 2>perceptron.err
clean:
	rm -r -f *~ *.out *.err *.log spark-warehouse

