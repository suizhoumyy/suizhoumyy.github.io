#!/bin/bash
echo $1
for i in $(find $1 -type f -name '*.jpeg'); do
    echo $i
done
