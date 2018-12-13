#!/bin/bash

echo `cut -f 1 hightemp.txt | sort | uniq -c | sort -r -n`