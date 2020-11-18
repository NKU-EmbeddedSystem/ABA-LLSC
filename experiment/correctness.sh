for solution in Pico-CAS HST HST-weak PST Pico-ST
do
	echo ""
	echo ""
	echo ""
	echo "--------------------------------------------------"
	echo "testing $solution"
	$(pwd)/../bin/$solution $(pwd)/../lock-free-stack-arm-asm/lockfree-stack -t 16 -l 10000
done
