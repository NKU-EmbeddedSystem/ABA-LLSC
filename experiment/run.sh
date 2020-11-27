mkdir -p logs/$1
rm logs/$1/*.txt
for program in blackscholes bodytrack facesim fluidanimate freqmine swaptions x264
do
	for thread in 1 2 4 8 16 32
	do
		for count in 1 2 3
		do
			parsecmgmt -a run -p $program -i simlarge -n $thread -s "time $(pwd)/../bin/$1" >> logs/$1/$program$thread.txt
		done
	done
done
