package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Println("Enter a number:")
	fmt.Scan(&n)

	var i, j int
	var flag bool

	fmt.Println("Prime numbers up to", n, "are:")

	for i = 2; i <= n; i++ {
		flag = false

		for j = 2; j <= i/2; j++ {
			if i%j == 0 {
				flag = true
				break
			}
		}

		if flag == false {
			fmt.Println(i)
		}
	}
}
