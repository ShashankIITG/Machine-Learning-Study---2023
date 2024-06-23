def set_pivot(array, low, high):
	pivot_value = array[high]
	i = low # track values less than pivot element 

	for j in range(low, high):
		if array[j]<pivot_value:
			array[i], array[j] = array[j], array[i]
			i += 1

	# set pivot after all element lower than it
	array[i], array[high] = array[high], array[i]
	return i


def quick_sort(array, low, high):
	if low < high:	
		pivot_index = set_pivot(array, low, high)

		# partition array over pivot element
		quick_sort(array, low, pivot_index-1)
		quick_sort(array, pivot_index+1, high)


if __name__ == '__main__':
	array=[30, 80, 10, 90, 40]
	quick_sort(array, 0, len(array)-1)

	for item in array:
		print(item, end=" ")
