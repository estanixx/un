#include <stdio.h>
#include <unistd.h>
int main(int agrc, char *args[]) {
  int fildes[2];
  // Create unnamed pipe
  if( pipe(fildes) < 0 ){
    perror("Error while creating pipe\n");
    return 1;
  }
  // Fork current process.
  if( fork() == 0 ){ /* Son process */
    int input = 200;
    write(fildes[1], &input, sizeof(int));
  }else{ /* Father process */
    int output;
    read(fildes[0], &output, sizeof(int));
    printf("El dato de salida es %d\n", output);
  }
  close(fildes[0]);
  close(fildes[1]);
  return 0;
}
