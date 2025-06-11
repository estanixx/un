#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
int main (int argc, char *argv[]){
  int *ptr = (int * ) malloc(sizeof(int) * 5);
  // Verificar si la asignación de memoria fue exitosa
  if (ptr == NULL) {
      printf("Error: No se pudo asignar memoria.\n");
      return 1;
  }
  printf("Ingres 5 números: \n");
  int temp;
  for (int i = 0; i < 5; i++){
    scanf("%d", &temp);
    memcpy(&ptr[i], &temp, sizeof(int));
  }
  for (int i = 0; i < 5; i++){
    printf("%p heap[%d] = %d\n", &ptr[i], i, ptr[i]);
  }
  free(ptr);
  return 0;
}