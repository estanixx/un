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
sem_t sem_p1_p2;
void *shm_ptr;

// Limpia los archivos abiertos.
void clean(){
  sem_close(&sem_p1_p2);
  shm_unlink(SHM_NAME);
}

// Función para generar pares-impares. -1 al terminar pares. -2 al terminar impares.
void p(char* fifo_name, int process_id, int initial_val, int req_nums){
  unlink(fifo_name);
  // P1 Crea y accede a tubería nombrada (Comunicación P3).
  int fd;
  if (mkfifo(fifo_name, 0666) == -1) {
    char* msg = sprintf("Error while creating P%d FIFO.\n", process_id);
    perror(msg);
    clean();
    exit(507); // Internal Error.
  }
  // Envía en ciclo N valores.
  int num;
  for (int i = 0; i < req_nums; i++){
    num = initial_val + (2 * i);
    sem_wait(&sem_p1_p2);
    memcpy(shm_ptr, &num, sizeof(int));
    sem_post(&sem_p1_p2);
  }
  num = -1 * process_id;
  memcpy(shm_ptr, &num, sizeof(int));
}

int main(){
  // Crea y accede a semáforo no-nombrado (Comunicación P1-P2).
  if (sem_init(&sem_p1_p2, 0, 1) == -1) {
    perror("Error while initializing sem_p1_p2.\n");
    exit(501); // Internal Error.
  }

  // Borra memoria compartida anterior.
  if (shm_unlink(SHM_NAME) == 0) {
    printf("Previous shared memory unlinked.\n");
  }

  // Crea y accede a memoria compartida (Comunicación P3).
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

  // Definición y recepción de parámetros de P1
  int N, a1, a2;
  printf("Ingrese el valor de N: ");
  scanf("%d", &N);
  printf("Ingrese el valor de a1: ");
  scanf("%d", &a1);
  printf("Ingrese el valor de a2: ");
  scanf("%d", &a2);

  // Valida datos recibidos. a1 par positivo. a2 impar positivo, N positivo.
  if(a1 % 2 != 0 || a1 <= 0 || a2 % 2 != 1  || a2 <= 0 || N <= 0){
    perror("Provided data isn't valid.\n");
    clean();
    exit(401); // Bad Request.
  }

  // Crea P2.
  pid_t pid = fork();
  if (pid < 0) {
    perror("Error while creating p2.\n");
    clean();
    exit(506); // Internal Error.
  }

  if (pid == 0) {
    /* P2 */
    p(P2_P3_FIFO_NAME, 2, a2, N);
  }else{
    /* P1 */
    p(P1_P3_FIFO_NAME, 1, a1, N);
  }

  // Finalmente limpiar.
  clean();
  return 0;
}