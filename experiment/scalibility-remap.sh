mkdir -p logs/PST-remap
for program in blackscholes bodytrack freqmine swaptions
do
	for thread in 1 2 4 8 16 32
	do
		for count in 1 2 3
		do
			parsecmgmt -a run -p $program -i simlarge -n $thread -s "time $(pwd)/../bin/PST-remap" >> logs/PST-remap/$program$thread.txt
		done
	done
done
