#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *args[]) {
  /* Se referencia la misma tuberia */
  const char mypipe[] = "/tmp/mypipe";
  /* Se abre la tuberia en modo lectura */
  int fd = open(mypipe, O_RDONLY);
  /* Variable para recibir el dato que sale */
  int dato_sale;
  /* Se lee el dato en la tuberia */
  printf("Esperando lectura...\n");
  read(fd, &dato_sale, sizeof(int));
  printf("Dato que sale de tubería: %d\n", dato_sale);
  /* Cerra el descriptor de archivo */
  close(fd);
  return 0;
}