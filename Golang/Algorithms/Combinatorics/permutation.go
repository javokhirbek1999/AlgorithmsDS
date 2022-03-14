// Permutation implementation

package main

import (
	"fmt"
)

func permutation(data []int, i int, length int) {
	if i == length {
		fmt.Println(data)
		return
	}

	for j := i; j < length; j++ {
		swap(data, i, j)
		permutation(data, i+1, length)
		swap(data, i, j)
	}
}

func swap(data []int, x int, y int) {
	data[x], data[y] = data[y], data[x]
}

func main() {
	arr := []int{1, 2, 3, 4}

	permutation(arr, 0, len(arr))
}
