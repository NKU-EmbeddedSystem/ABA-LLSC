echo "--------------------------------------------------"
echo "testing Pico-HTM"
echo "--------------------------------------------------"
$(pwd)/../bin/Pico-HTM $(pwd)/../lock-free-stack-arm-asm/lockfree-stack -t 16 -l 10000
echo ""
echo ""
echo ""
echo "--------------------------------------------------"
echo "testing HST-HTM"
echo "--------------------------------------------------"
$(pwd)/../bin/HST-HTM $(pwd)/../lock-free-stack-arm-asm/lockfree-stack -t 16 -l 5000
