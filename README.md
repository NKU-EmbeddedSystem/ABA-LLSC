# Workflow of QEMU-ABA

- **Note1:** This is the code and scripts for paper "Enhancing Atomic Instruction Emulation for Cross-ISA Dynamic Binary Translation" at CGO 2021.
- **Note2:** This repo is archived for Artifact Evaluation usage so you can not open an issue. Nevertheless, if you have any problem or suggestion, please feel free to contact us. Eg. troppingz at gmail dot com

## Setup environment
### Fetch code
fetch build and experiment scripts
```
git clone https://github.com/NKU-EmbeddedSystem/ABA-LLSC.git
cd ABA-LLSC
```
fetch source code
```
git clone https://github.com/NKU-EmbeddedSystem/QEMU-ABA.git
```
fetch corressness verification code
```
git clone https://github.com/NKU-EmbeddedSystem/lock-free-stack-arm-asm.git
```

### Hardware
HST-HTM and Pico-HTM need Hardware Transactions Memory(HTM) support like Intel TSX
### Run-time environment
Linux-5.4 Ubuntu20.04
### Install Dependencies
sudo bash installDep.sh

## Build
build HST, HST-weak, PST, PST-remap and Pico-CAS and Pico-ST
``` 
bash build.sh
```

if HTM supported, you can build Pico-HTM and HST-HTM
```
bash build-HTM.sh
```

## Run
Make sure parsec-3.0 installed and environment 

Make sure you have built the binaries. 
```
cd experiment
```

### Scalibility Evaluate

Profile HST, HST-weak, PST, Pico-CAS, and Pico-ST elapsed time. It may take loong time because PST and Pico-ST are too slow.
```
bash scalibility.sh
```
If you only want to profile just one solutions such as HST
```
bash run.sh HST
```

If HTM supported, you can also evaluate HST-HTM
```
bash scalibility-HTM.sh
```

When the scripts finish, use the following scripts to analyse the logs and generate the csvs of elapsed time. 

```
python3 elapsed-time.py
cat elapsed-time.csv
```
If HTM supported
```
python3 elapsed-time-HTM.py
cat elapsed-time-HTM.csv
```

### Correctness Evaluate
We use a lock free stack in arm to evaluate the correctness. 

```
bash correctness.sh
```
If HTM supported
```
bash correctness-HTM.sh
```

### Drawing Speedup figures

#### 1. Normalize data to speedup
We first use `speedup.py` under `experiment` folder to normalize data to single thread execution time of Pico-CAS.

```
cd experiment
python3 ./speedup.py
```

This generates `speedup.csv`.

#### 2. Drawing figure

We use `draw.py` to generate pdf file.
```
python3 ./draw.py
```

You should see a figure like this, called `speedup.pdf`:
![Speedup](speedup-sample.png)

## Troubleshooting

If you have any problem or suggestion, please feel free to contact us. Eg. troppingz at gmail dot com
