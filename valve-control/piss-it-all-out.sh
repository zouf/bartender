#!/bin/bash

for i in `seq 0 7`
do 
   sleep 1
   echo $i
  gpio write $i 1
done

for i in `seq 17 20`
do
  gpio write $i 1
done

sleep 2

for i in `seq 0 7`
do
  gpio write $i 0
done

gpio write 2 1

for i in `seq 17 20`
do
  gpio write $i 0
done

sleep 1

gpio write 2 0


