#!/bin/bash

for i in `seq 0 7`
do
  gpio mode $i out
done

for i in `seq 17 20`
do
  gpio mode $i out
done
