cd QEMU-ABA

git checkout Pico-HTM
../configure.sh
echo "Pico-HTM"
make -j40
cp arm-linux-user/qemu-arm ../bin/Pico-HTM

git checkout HST-HTM
../configure.sh 2>&1 >/dev/null
echo "HST-HTM"
make -j40
cp arm-linux-user/qemu-arm ../bin/HST-HTM
