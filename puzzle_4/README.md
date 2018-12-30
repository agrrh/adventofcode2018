```
# organize input
cat input.txt | sed 's/-/ /g' | sort -k1 -k2 -k3 -k4 | sed -E 's/1518 ([0-9]{2}) ([0-9]{2})/1518-\1-\2/g' > input_sorted.txt

# slept longer
python3 main.py | sort -k 2 -r -n | head -n1

# most frequent sleep in same min
python3 main.py | sort -k 4 -r -n | head -n1
```
