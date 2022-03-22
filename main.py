first = 0
second = 1

arr = [0,1]
stepSec = int(input('How many numbers you want from the fibonacci series?: '))
if stepSec > 0:
	theonestep = int(input('Tell me the nth number: '))

if stepSec == 0:
	print('Nothing')
elif stepSec == 1:
	print(arr[0])
elif stepSec == 2:
	print(arr)
elif stepSec < 0:
	print("Negative values are not ")
else:
	for i in range(stepSec-2):
		arr.append(arr[-1]+arr[-2])
	print(str(arr))

if stepSec > 0:
	print(f'The {theonestep}th one is: {arr[theonestep-1]}')
