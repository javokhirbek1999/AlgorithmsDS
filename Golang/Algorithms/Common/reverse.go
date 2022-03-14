// Reverse in-place

func reverse(arr []int) {
	start, end := 0, len(arr)-1

	for start < end {
		arr[start], arr[end] = arr[end], arr[start]
		start++
		end--
	}
}

