for solution in Pico-HTM HST-HTM
do
	echo ""
	echo ""
	echo ""
	echo "--------------------------------------------------"
	echo "testing $solution"
	$(pwd)/../bin/$solution $(pwd)/../lock-free-stack-arm-asm/lockfree-stack -t 16 -l 10000
done
