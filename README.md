# ng-py
My Number Generator (From JavaScript ported to Python)

## Running
```python
# Create a new variable
newin = NumberGenerator().filter(length_of_number, start_filter_number)

newin = NumberGenerator().filter(8,8)
# The code above will return 8 digit numbers that start with 8

# Real Usage:
for x in range(0,9):
    # print
    newin = NumberGenerator().filter(8,8)
    
# Expected Output:
# Minimum of 0 outputs to upto 10 outputs
# I ran the code above several times and got these:
# 89465075
# 81678559

```
