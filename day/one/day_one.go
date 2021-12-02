package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func read_file() []string {
    data, err := ioutil.ReadFile("input.txt")
    if err != nil {
        fmt.Printf("Error reading file: %s", err)
    }
    return strings.Split(string(data), "\n")
}

func str_to_int(str string) int {
    integer, err := strconv.Atoi(str)
    if err != nil {
        fmt.Printf("Error converting '%s' to int: %s", str, err)
    }
    return integer
}

func part_one(data []string) int {
    increases := 0
    last := str_to_int(data[0])
    for i:= 1; i < len(data)-1; i++ {  // len-1 for one blank line result of split 
        current := str_to_int(data[i])
        if current > last {
            increases++
        }
        last = current
    }
    return increases
}

func part_two(data []string) int {
    var sliding_window []int
    increases := 0
    for i:= 0; i < len(data)-3; i++ {
        sliding_window = append(sliding_window, str_to_int(data[i])+str_to_int(data[i+1])+str_to_int(data[i+2]))
        if i>0 && sliding_window[i] > sliding_window[i-1] {
            increases++
        }
    }
    return increases
}


func main() {
    data := read_file()
    fmt.Println(part_one(data))
    fmt.Println(part_two(data))
}
