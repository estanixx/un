#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <string.h>
#include <fcntl.h> // Para las constantes O_* y mode_t
#include <semaphore.h>
// Definición de constantes para los nombres de los FIFOs y el shm
#define SHM_NAME "/p1-p2-p3"
#define P1_P3_FIFO_NAME "/tmp/fifo_p1_p3"
#define P2_P3_FIFO_NAME "/tmp/fifo_p2_p3"
#define P3_SEM_NAME "/sem_p3"
#define P2_SEM_NAME "/sem_p2"
#define P1_SEM_NAME "/sem_p1"
#define AUX_SEM_NAME "/sem_aux"

// Variables globales para los identificadores
int *shm_ptr = NULL; // Apuntador a la memoria compartida
int shm_fd = -1;     // Descriptor de archivo para el shm
int fifo_p1_p3 = -1; // Descriptor de archivo para el FIFO p1_p3
int fifo_p2_p3 = -1; // Descriptor de archivo para el FIFO p2_p3
sem_t *sem_p3, *sem_p2, *sem_p1, *sem_aux;

// Función para limpiar recursos (cerrar FIFOs y shm)
void cleanup()
{
  // Desmontar la memoria compartida
  if (munmap(shm_ptr, sizeof(int)) == -1)
  {
    perror("Error al desmontar el shm");
    exit(1);
  }

  // Cerrar el descriptor del shm
  if (shm_fd != -1)
  {
    close(shm_fd);
  }

  // Eliminar los FIFOs y semáforos
  unlink(P1_P3_FIFO_NAME);
  unlink(P2_P3_FIFO_NAME);
  sem_unlink(AUX_SEM_NAME);
  sem_unlink(P1_SEM_NAME);
  sem_unlink(P2_SEM_NAME);
  sem_unlink(P3_SEM_NAME);
}

// Función para manejar errores
void handle_error(const char *message)
{
  perror(message);
  cleanup();
  exit(1);
}

// Función para crear y acceder a los FIFOs y el shm
void create_and_access_fifos_and_shm()
{
  sem_p3 = sem_open(P3_SEM_NAME, O_CREAT | O_EXCL, 0666, 0);
  // Permisos 666, valor inicial 1
  if (sem_p3 == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }
  sem_p2 = sem_open(P2_SEM_NAME, O_CREAT | O_EXCL, 0666, 1);
  // Permisos 666, valor inicial 1
  if (sem_p2 == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }
  sem_p1 = sem_open(P1_SEM_NAME, O_CREAT | O_EXCL, 0666, 1);
  // Permisos 666, valor inicial 1
  if (sem_p1 == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }
  sem_aux = sem_open(AUX_SEM_NAME, O_CREAT | O_EXCL, 0666, 1);
  // Permisos 666, valor inicial 1
  if (sem_aux == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }

  // Crear los FIFOs
  if (mkfifo(P1_P3_FIFO_NAME, 0666) == -1)
  {
    handle_error("Error al crear el FIFO p1_p3");
  }
  if (mkfifo(P2_P3_FIFO_NAME, 0666) == -1)
  {
    handle_error("Error al crear el FIFO p2_p3");
  }
  // Crear el segmento de memoria compartida (shm)
  shm_fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
  if (shm_fd == -1)
  {
    handle_error("Error al crear el shm");
  }

  // Establecer el tamaño del shm
  if (ftruncate(shm_fd, sizeof(int)) == -1)
  {
    handle_error("Error al establecer el tamaño del shm");
  }

  // Mapear el shm a la memoria del proceso
  shm_ptr = mmap(
      NULL,
      sizeof(int),
      PROT_READ | PROT_WRITE,
      MAP_SHARED,
      shm_fd,
      0);
  if (shm_ptr == MAP_FAILED)
  {
    handle_error("Error al mapear el shm");
  }

  // Uso la flag "-4" en memoria compartida para indicar a p1 que p3 está en
  // ejecución.
  *shm_ptr = -4;
  // Acceder a los FIFOs (ejemplo simple de escritura y lectura)
  // Abrir FIFO p1_p3 para escribir
  fifo_p1_p3 = open(P1_P3_FIFO_NAME, O_WRONLY);
  if (fifo_p1_p3 == -1)
  {
    handle_error("Error al abrir el FIFO p1_p3");
  }

  fifo_p2_p3 = open(P2_P3_FIFO_NAME, O_WRONLY);
  if (fifo_p2_p3 == -1)
  {
    handle_error("Error al abrir el FIFO p2_p3");
  }
}

int main()
{
  // Crear y acceder a los FIFOs y el shm
  cleanup();
  printf("Esperando por P1 y P2.\n");
  create_and_access_fifos_and_shm();
  int p1_running = 1;
  int p2_running = 1;
  while (p1_running || p2_running)
  {
    sem_wait(sem_p3);
    int val = *shm_ptr;
    printf("%d ", val);
    fflush(stdout);

    if (val == -1)
    {
      p1_running = 0;
      if (p2_running)
      {
        sem_post(sem_p1);
      }
    }
    else if (val == -2)
    {
      p2_running = 0;
      if (p1_running)
      {
        sem_post(sem_p2);
      }
    }
    else if (val % 2 == 0)
    {
      sem_post(sem_p1);
    }
    else
    {
      sem_post(sem_p2);
    }
  }
  int msg = -3;
  if (write(fifo_p1_p3, &msg, sizeof(int)) == -1)
  {
    handle_error("Error al escribir en fifo");
  }
  sem_post(sem_p1);
  if (write(fifo_p2_p3, &msg, sizeof(int)) == -1)
  {
    handle_error("Error al escribir en fifo");
  }
  sem_post(sem_p2);

  printf("\n-3 P3 termina\n");
  // Limpiar recursos
  cleanup();

  return 0;
}
