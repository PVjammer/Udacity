package main

import(
  "fmt";

)

func fib(x int) int{
  f := []int{0,1}
  if x ==0{return 0}
  if x ==1{
    return 1
  } else {
    for i:=2; i <=x; i++{
      f = append(f,f[i-1]+f[i-2])
    }
  }
  return f[len(f)-1]
}

func main(){
  fmt.Println(fib(10))
}
