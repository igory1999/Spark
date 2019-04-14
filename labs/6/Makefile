generate:
	python generate_commands.py
stream:	
	bash mystream.sh
nc:	
	bash mync.sh
csv:
	mkdir -p input_csv
age:	csv
	spark-submit --master local[3] --name 'Streaming word count example' age.py 2>age.err
clean:
	rm -r -f *~ *.out *.err *.log spark-warehouse mync.sh mystream.sh
	mv input_csv/*.csv tmp/


