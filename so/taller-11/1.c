#include <stdio.h>
 #include <unistd.h>
#include <stdlib.h>
int main (int argc, char *argv[]){
  int x = 3; //Gracias Faryd por este dato
  printf("Codigo: %p\n", main);
  printf("Heap: %p\n", malloc(10));
  printf("Stack: %p\n", &x);
  while(1){
    sleep(1);
  }
  return 0;
}