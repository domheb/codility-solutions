# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
	list_of_ones = []
	number_of_elements = 0
	bin_number = []

	if not isinstance(N, int): #check if N is an intiger
		return(-1)

	if N == 1 or N == 0: #check if N is equal to 0 or 1
		return(0)	
	else:
		bin_number.append(1) #every next bin number starts with 1
		reverse_bin_number = [] #all the next 0 and 1 would need to be reversed
		while (N != 1):
			temp = N % 2
			reverse_bin_number.append(temp)
			N = N // 2

	length = len(reverse_bin_number)

	for i in range(length-1,-1,-1):
		bin_number.append(reverse_bin_number[i]) #here they are reversed

	length = len(bin_number)
	binary_gap = 0
	binary_gap_max = 0
	is_counting = 0

	for i in range(0,length):
		#1) start counting
		if is_counting == 0 and bin_number[i] == 1:
			is_counting = 1
			continue
		#2) continue counting
		if is_counting == 1 and bin_number[i] == 0:
			binary_gap +=1
			continue
		#3) stop counting
		if is_counting == 1 and bin_number[i] == 1:
			if binary_gap > binary_gap_max:
				binary_gap_max = binary_gap
			binary_gap = 0
			continue

	return(binary_gap_max)

print(solution(805306373))
