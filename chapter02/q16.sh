#!/bin/bash

echo -n "分割数は？"
read n

count=`wc -l hightemp.txt | cut -f 1 --delim=" "`
echo $count
num_lines=`expr $count / $n`
remainder=`expr $count % $n`

echo $num_lines
echo $remainder

if [ $remainder -gt 0 ]; then
    num_lines=`expr $num_lines + 1`
fi

split -l $num_lines hightemp.txt paragraph
