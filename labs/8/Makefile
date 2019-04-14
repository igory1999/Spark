lenet_local:
	sbatch lenet_local.batch
	sleep 5
	squeue -u $(USER)
lenet5:
	mkdir -p model
	sbatch lenet5.batch
	sleep 5
	squeue -u $(USER)
clean:
	rm -rf *.out *.err *.log *~ metastore_db logs checkpoints model mnist_data
