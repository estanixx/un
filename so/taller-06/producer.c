#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *args[]) {
  const char mypipe[] = "/tmp/mypipe";
  printf("Proceso de pipe.\n");
  /* Delete possibly former pipes */
  /*Create the pipe connection*/
  if (mkfifo (mypipe, 0666) < 0) {
    perror("Error al crear la tubería\n");
    return (1);
  }
  /* Abrir la tuberia para escritura */
  int fd = open (mypipe, O_WRONLY);
  /* Dato que entra a la tuberia */
  int dato_entra = 200;
  /* Escribir el dato en la tuberia */
  printf("Proceso de escritura.\n");
  write(fd, &dato_entra, sizeof(int));
  /* Cerrar el descriptor de archivo */
  close (fd);
  return 0;
}