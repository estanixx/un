#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <string.h>
#include <semaphore.h>
#include <pthread.h>
#include <sys/mman.h> // Para memoria compartida
#include <sys/wait.h>

// Definición de constantes para los nombres de los FIFOs y el shm
#define SHM_NAME "/p1-p2-p3"
#define P1_P3_FIFO_NAME "/tmp/fifo_p1_p3"
#define P2_P3_FIFO_NAME "/tmp/fifo_p2_p3"
#define P3_SEM_NAME "/sem_p3"
#define P2_SEM_NAME "/sem_p2"
#define P1_SEM_NAME "/sem_p1"
#define AUX_SEM_NAME "/sem_aux"

// Variables globales para los identificadores
int *shm_ptr = NULL;                       
// Apuntador a la memoria compartida
int shm_fd = -1;                           
// Descriptor de archivo para el shm
int fifo_p1_p3 = -1;                       
// Descriptor de archivo para el FIFO p1_p3
int fifo_p2_p3 = -1;                      
// Descriptor de archivo para el FIFO p2_p3
sem_t *sem_p1, *sem_p2, *sem_aux, *sem_p3; 
// Semáforos para alternar y el de inicio

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

  // Eliminar los FIFOs
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

  sem_p3 = sem_open(P3_SEM_NAME, 0); // Permisos 666, valor inicial 1
  if (sem_p3 == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }
  sem_p2 = sem_open(P2_SEM_NAME, 0); // Permisos 666, valor inicial 1
  if (sem_p2 == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }
  sem_p1 = sem_open(P1_SEM_NAME, 0); // Permisos 666, valor inicial 1
  if (sem_p1 == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
  }
  sem_aux = sem_open(AUX_SEM_NAME, 0); // Permisos 666, valor inicial 1
  if (sem_aux == SEM_FAILED)
  {
    handle_error("Error al crear el semáforo");
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
  shm_ptr = mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd,
  0);
  if (shm_ptr == MAP_FAILED)
  {
    handle_error("Error al mapear el shm");
  }
  if (*shm_ptr != -4)
  {
    handle_error("P3 no está en ejecución");
  }
  // Acceder a los FIFOs (ejemplo simple de escritura y lectura)
  // Abrir FIFO p1_p3 para escribir
  fifo_p1_p3 = open(P1_P3_FIFO_NAME, O_RDONLY);
  if (fifo_p1_p3 == -1)
  {
    handle_error("Error al abrir el FIFO p1_p3");
  }

  fifo_p2_p3 = open(P2_P3_FIFO_NAME, O_RDONLY);
  if (fifo_p2_p3 == -1)
  {
    handle_error("Error al abrir el FIFO p2_p3");
  }
}

// Funciones-generador de numeros
void gen_even(int init, int n)
{
  int aux_val;
  sem_getvalue(sem_aux, &aux_val);
  if (aux_val == 1)
  {
    sem_wait(sem_aux);
    sem_wait(sem_p2);
  }

  for (int i = 0; i < n; i++)
  {
    sem_wait(sem_p2);
    *shm_ptr = init + (2 * i);
    sem_post(sem_p3);
  }
  sem_wait(sem_p2);
  *shm_ptr = -1;
  sem_post(sem_p3);
  sem_wait(sem_p2);
  int data;
  if(read(fifo_p2_p3, &data, sizeof(int)) == -1){
    handle_error("Error al leer de fifo");
  }
  printf("-3 P1 termina\n");
}

void gen_odd(int init, int n)
{
  int aux_val;
  sem_getvalue(sem_aux, &aux_val);
  if (aux_val == 1)
  {
    sem_wait(sem_aux);
    sem_wait(sem_p1);
  }
  for (int i = 0; i < n; i++)
  {
    sem_wait(sem_p1);
    *shm_ptr = init + (2 * i);
    sem_post(sem_p3);
  }
  sem_wait(sem_p1);
  *shm_ptr = -2;
  sem_post(sem_p3);
  sem_wait(sem_p1);
  int data;
  if(read(fifo_p2_p3, &data, sizeof(int)) == -1){
    handle_error("Error al leer de fifo");
  }
  printf("-3 P2 termina\n");
}
// función para validar datos internos.
void validate_data(int argc, char *argv[], int *N, int *a1, int *a2)
{
  if (argc != 4)
  {
    handle_error("Uso: p1 N a1 a2");
  }
  // Convertir argumentos a enteros
  *N = atoi(argv[1]);
  *a1 = atoi(argv[2]);
  *a2 = atoi(argv[3]);

  // Validar restricciones específicas
  if (*N <= 0 || *a1 <= 0 || *a2 <= 0)
  {
    handle_error("Error: N, a1, y a2 deben ser mayores que cero.");
  }
  if (*a2 % 2 == 0)
  {
    handle_error("Error: a2 debe ser un número impar.");
  }
  if (*a1 % 2 != 0)
  {
    handle_error("Error: a1 debe ser un número par.");
  }
}
int main(int argc, char *argv[])
{
  // Validamos los datos ingresados
  int N, a1, a2;
  validate_data(argc, argv, &N, &a1, &a2);
  // Crear y acceder a los FIFOs y el shm
  create_and_access_fifos_and_shm();

  pid_t pid = fork();
  if (pid == -1)
  {
    handle_error("Error en la creación de P2");
  }
  else if (pid == 0)
  {
    /* P2 */

    gen_odd(a2, N);
  }
  else
  {
    /* P1 */
    gen_even(a1, N);

    // Limpiar recursos
    cleanup();

    return 0;
  }
}
