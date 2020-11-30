cd lock-free-stack-arm-asm
make
cd ..
cd QEMU-ABA
git checkout PST
../configure.sh
make clean 2>&1 >/dev/null
echo "PST "
make -j40
cp arm-linux-user/qemu-arm ../bin/PST

git checkout PST-remap
../configure.sh 2>&1 >/dev/null
make clean 2>&1 >/dev/null
echo "PST-remap"
make -j40
cp arm-linux-user/qemu-arm ../bin/PST-remap

git checkout HST
../configure.sh 2>&1 >/dev/null
make clean 2>&1 >/dev/null
echo "HST"
make -j40
cp arm-linux-user/qemu-arm ../bin/HST

git checkout HST-weak
../configure.sh 2>&1 >/dev/null
make clean 2>&1 >/dev/null
echo "HST-weak"
make -j40
cp arm-linux-user/qemu-arm ../bin/HST-weak

git checkout Pico-CAS
../configure.sh 2>&1 >/dev/null
make clean 2>&1 >/dev/null
echo "Pico-CAS"
make -j40
cp arm-linux-user/qemu-arm ../bin/Pico-CAS

git checkout Pico-ST
../configure.sh 2>&1 >/dev/null
make clean 2>&1 >/dev/null
echo "Pico-ST"
make -j40
cp arm-linux-user/qemu-arm ../bin/Pico-ST
