top -b -d$2 -p $1 > out
cat out  | grep $1 | awk '{ print $9 " " $10 }' | nl -i $2> out_cpu_mem
