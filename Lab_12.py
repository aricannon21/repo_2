#function to split list into 2
def split_list(input_list):
	if (len(input_list)==1):
		print("Delivering to " + input_list[0])
	else:
		mid = len(input_list) // 2
	
		input_list_1st_half = input_list[:mid]
		input_list_2nd_half = input_list[mid:]
		split_list(input_list_1st_half)
		split_list(input_list_2nd_half)

#function of fib using while loop
def fib(n):
	a = 1
	b = 1
	count = 0

	while(count < n):
		count+=1
		old_a = a
		a = b
		b = old_a + b
	return(a)

#function of fib using recursion (not always the best way), but can reduce lines of code / it is simpler
def fib_recursive(n):
	#base case
	if(n <= 1):
		return(1)
	else:
		return(fib_recursive(n-1)+fib_recursive(n-2))
		
#call functions
def main():
	list_1 = ['House_1', 'House_2', 'House_3', 'House_4']
	split_list(list_1)

	# print(christmas_fact(n = 4))
	print(fib(n=0))
	print(fib(n=1))
	print(fib(n=2))
	print(fib(n=5))
	print(fib_recursive(n=0))
	print(fib_recursive(n=1))
	print(fib_recursive(n=2))
	print(fib_recursive(n=5))


if __name__ == '__main__':
	main()