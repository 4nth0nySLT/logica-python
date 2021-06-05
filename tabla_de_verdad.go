package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"time"
)

func tabla_bruta(numero2 string) int {
	start := time.Now()
	numero, _ := strconv.Atoi(numero2)
	f := float64(numero)
	total := math.Pow(2, f)
	total_u := int(total)
	println("Posibilidades:", total_u)
	memoria := total_u
	matriz := []int{}
	for i := 1; i < numero+1; i++ {
		ceros := memoria / 2
		veces := total_u / ceros
		for index := 0; index < veces; index++ {
			valor := index % 2
			for x := 0; x < ceros; x++ {
				matriz = append(matriz, valor)
			}
		}
		memoria = memoria / 2
	}
	duration := time.Since(start)
	fmt.Println(duration.Seconds())
	return 0
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		os.Exit(tabla_bruta(args[0]))
	} else {
		os.Exit(0)
	}
}
