// + build main1
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func randValueGenerator(mnValue int, mxValue int) int {
	return mnValue + rand.Intn(mxValue-mnValue)
}

func main() { // +build main1
	values := []int{}
	for i := range make([]int, 10000) {
		randomValues := randValueGenerator(-1000, 1000)
		values = append(values, randomValues)
		i++
	}

	initiateMergeSort(values)
	initiateInsertion(values)

}

func initiateMergeSort(arr []int) {
	timeStart := time.Now()
	fmt.Println("\n" + "Merge Sort:")
	subArray(arr)
	sortingArray(arr)
	timeSince := time.Since(timeStart)
	//fmt.Println(arr)
	fmt.Println("Time elapsed of the programe:", timeSince)
}

func initiateInsertion(arr []int) {
	timeStart := time.Now()
	fmt.Println("\n \n" + "Insertion Sort:")
	insertionSort(arr)
	timeSince := time.Since(timeStart)
	fmt.Println(arr)
	fmt.Println("Time elapsed of the programe:", timeSince)

}

func insertionSort(arr []int) {

	for j := 0; j < len(arr); j++ {
		key := arr[j]

		i := j - 1
		for i >= 0 && arr[i] > key {
			arr[i+1] = arr[i]
			i = i - 1
		}

		arr[i+1] = key
	}

}

func sortingArray(arr []int) []int {

	if len(arr) == 1 {
		return arr
	}
	divide := len(arr) / 2

	part1 := arr[:divide]
	part2 := arr[divide:]
	//Send into function again to split again
	part1 = sortingArray(part1)
	part2 = sortingArray(part2)

	return mergeSort(part1, part2)

}
func mergeSort(arr1, arr2 []int) []int {
	var mergedArray []int

	for len(arr1) > 0 || len(arr2) > 0 {
		//If mArray and mArray2 larger than 0
		if len(arr1) > 0 && len(arr2) > 0 {
			if arr1[0] > arr2[0] {
				mergedArray = append(mergedArray, arr2[0])
				arr2 = arr2[1:]
			} else {
				mergedArray = append(mergedArray, arr1[0])
				arr1 = arr1[1:]
			}
		} else if len(arr1) > 0 {
			mergedArray = append(mergedArray, arr1[0])
			arr1 = arr1[1:]
		} else if len(arr2) > 0 {
			mergedArray = append(mergedArray, arr2[0])
			arr2 = arr2[1:]
		}
	}

	return mergedArray
}

func subArray(arr []int) []int {
	mxValueStart := 0
	mxValueEnd := 0
	for i := range make([]int, 1000) {
		mxValueEnd = mxValueEnd + arr[i]
		if mxValueEnd < 0 {
			mxValueEnd = 0
		} else if mxValueStart < mxValueEnd {
			mxValueStart = mxValueEnd
		}

	}
	fmt.Println("Maximum subarray: ", mxValueStart)

	return arr
}
