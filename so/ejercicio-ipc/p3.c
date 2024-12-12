#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <string.h>

#define SHM_NAME "/p1-p2-p3"
#define P1_P3_FIFO_NAME "/tmp/fifo_p1_p3"
#define P2_P3_FIFO_NAME "/tmp/fifo_p2_p3"

void *shm_ptr;
int main(){
  // Crea y accede a memoria compartida (Comunicación P1-P2).
  int shm_fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
  if (shm_fd == -1) {
    perror("Error while creating the shared memory.\n");
    clean();
    exit(502); // Internal Error.
  }
  
  // Ajusta el tamaño de la memoria a sizeof(int).
  if (ftruncate(shm_fd, sizeof(int)) == -1) {
    perror("Error while adjusting shared memory size.\n");
    clean();
    exit(503); // Internal Error.
  }

  // Mapear la memoria compartida en el espacio de direcciones
  shm_ptr = mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
  if (shm_ptr == MAP_FAILED) {
    perror("Error while mapping the shared memory.\n");
    clean();
    exit(504); // Internal Error.
  }
  int p1_finished = 0;
  int p2_finished = 0;
  // TODO: Muestra datos recibidos.
  while(1){

  }
  // TODO: Accede a tubería nombrada (Comunicación P1).
  // TODO: Accede a tubería nombrada (Comunicación P2).
  // TODO: Accede a memoria compartida de tamaño sizeof(int) (Comunicación P2).
  // TODO: Al recibir -1 y -2, envía -3 por tubería.
  return 0;
}