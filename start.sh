#!/bin/bash
echo $(date)
for i in {0..5}
do
	python client.py $i &
done
