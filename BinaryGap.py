"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(N):

    #Create useful variables
	bin_number = []

    #Check possibilities:
	if not isinstance(N, int): #Case 1: N is not an intiger
		return(-1)
	if N == 1 or N == 0: #Case 2: N is equal to 0 or 1 so no gap
		return(0)		
	else:
		bin_number.append(1) #bin_number always starts with 1
		reverse_bin_number = [] #all the next 0 and 1
		while (N != 1):			#would need to be reversed first
			temp = N % 2
			reverse_bin_number.append(temp)
			N = N // 2

	#Perform reversing
	length = len(reverse_bin_number)
	for i in range(length-1,-1,-1):
		bin_number.append(reverse_bin_number[i]) #here they are reversed
	length += 1 #bin_number has 1 more element -> the first one

	#Perform main operation
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
			if binary_gap > binary_gap_max: #maximize binary_gap_max if possible
				binary_gap_max = binary_gap
			binary_gap = 0
			continue

	return(binary_gap_max)
