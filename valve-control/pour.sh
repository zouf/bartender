#!/bin/bash

gpio write $1 1

sleep $2

gpio write 2 1

gpio write $1 0

sleep 2

gpio write 2 0


