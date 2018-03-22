#statistics
#1. read the file
with open('stats.txt') as fin:
    for i, line in enumerate(fin):
        if i < 10:
            line = line.strip().split(',')

            func, *nums,  = line
            nums = [int(i) for i in nums]

            print(i, nums, func)

#2. break apart the line in components (split)
# 2a. extract the function name
# 2b. convert the string numbers to legit numbers
#3. figure out the function...
#4. perform that function on the numbers
