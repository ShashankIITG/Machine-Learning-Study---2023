def merge(left, right):
	l, r = 0, 0
	result = []
	while l < len(left) and r < len(right):
		try:
			if left[l] <= right[r]:
				result.append(left[l])
				l += 1
			else:
				result.append(right[r])
				r += 1
		except:
			pass

	if l < len(left):
		[result.append(i) for i in left[l:]]
	if r < len(right):
		[result.append(i) for i in right[r:]]

	return result

def merge_sort(array):
	if len(array) <= 1:
		return array

	half = len(array) // 2
	left = merge_sort(array[:half])
	right = merge_sort(array[half:])

	return merge(left, right)


if __name__ == '__main__':
	array=[30, 80, 10, 90, 40, 20]
	result = merge_sort(array)

	for item in result:
		print(item, end=" ")