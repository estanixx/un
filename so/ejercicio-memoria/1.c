#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/time.h>
#include <string.h>

#define PAGE_SIZE 4096  // 4 KiB
#define VIRTUAL_ADDRESS_SPACE 32

unsigned char* TLB = NULL; // Puntero al TLB (memoria dinámica)
int TLB_ENTRY_SIZE = 4 * sizeof(unsigned int) + (21 + 13) * sizeof(unsigned char); // Tamaño de una entrada del TLB
int TLB_size = 0; // Número actual de entradas en el TLB

// Función para verificar si una dirección es válida.
bool is_valid_address(unsigned int address) {
  return address < (1ULL << VIRTUAL_ADDRESS_SPACE);
}

// Función para obtener el número de página a partir de una dirección.
unsigned int get_page_number(unsigned int address) {
  return address / PAGE_SIZE;
}

// Función para obtener el desplazamiento dentro de la página.
unsigned int get_offset(unsigned int address) {
  return address % PAGE_SIZE;
}

// Función para establecer la dirección en una entrada del TLB.
void set_entry_address(int index, unsigned int address) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE);
  *((unsigned int*) field) = address;
}

// Función para obtener la dirección de una entrada del TLB.
unsigned int get_entry_address(int index) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE);
  return *((unsigned int*) field);
}

// Función para establecer el número de página en una entrada del TLB.
void set_entry_page_number(int index, unsigned int page_number) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + sizeof(unsigned int);
  *((unsigned int*) field) = page_number;
}

// Función para obtener el número de página de una entrada del TLB.
unsigned int get_entry_page_number(int index) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + sizeof(unsigned int);
  return *((unsigned int*) field);
}

// Función para establecer el desplazamiento en una entrada del TLB.
void set_entry_offset(int index, unsigned int offset) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 2 * sizeof(unsigned int);
  *((unsigned int*) field) = offset;
}

// Función para obtener el desplazamiento de una entrada del TLB.
unsigned int get_entry_offset(int index) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 2 * sizeof(unsigned int);
  return *((unsigned int*) field);
}

// Función para establecer el número de página en binario en una entrada del TLB.
void set_entry_page_binary(int index, unsigned char* page_binary) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 3 * sizeof(unsigned int);
  strcpy((char*) field, page_binary);
}

// Función para obtener el número de página en binario de una entrada del TLB.
unsigned char* get_entry_page_binary(int index) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 3 * sizeof(unsigned int);
  return (unsigned char*) field;
}

// Función para establecer el desplazamiento en binario en una entrada del TLB.
void set_entry_offset_binary(int index, unsigned char* offset_binary) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 3 * sizeof(unsigned int) + 21 * sizeof(unsigned char);
  strcpy((char*) field, offset_binary);
}

// Función para obtener el desplazamiento en binario de una entrada del TLB.
unsigned char* get_entry_offset_binary(int index) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 3 * sizeof(unsigned int) + 21 * sizeof(unsigned char);
  return (unsigned char*) field;
}

// Función para establecer la última iteración de acceso en una entrada del TLB.
void set_entry_last_access_iteration(int index, unsigned int last_access_iteration) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 3 * sizeof(unsigned int) + (21 + 13) * sizeof(unsigned char);
  *((unsigned int*) field) = last_access_iteration;
}

// Función para obtener la última iteración de acceso de una entrada del TLB.
unsigned int get_entry_last_access_iteration(int index) {
  unsigned char* field = TLB + (index * TLB_ENTRY_SIZE) + 3 * sizeof(unsigned int) + (21 + 13) * sizeof(unsigned char);
  return *((unsigned int*) field);
}

// Función para inicializar el TLB.
void initialize_TLB() {
  TLB = (unsigned char*) malloc(5 * TLB_ENTRY_SIZE);
  if (TLB == NULL) {
    perror("Failed to allocate memory for TLB");
    exit(EXIT_FAILURE);
  }
  TLB_size = 0;
}

// Función para liberar la memoria del TLB.
void free_TLB() {
  free(TLB);
}

// Función para añadir una entrada al TLB.
void add_to_TLB(unsigned int address, unsigned int page_number, unsigned int offset, unsigned char* page_binary, unsigned char* offset_binary, unsigned int last_access_iteration) {
  if (TLB_size < 5) {
    set_entry_address(TLB_size, address);
    set_entry_page_number(TLB_size, page_number);
    set_entry_offset(TLB_size, offset);
    set_entry_page_binary(TLB_size, page_binary);
    set_entry_offset_binary(TLB_size, offset_binary);
    set_entry_last_access_iteration(TLB_size, last_access_iteration);
    TLB_size++;
    printf("Politica de reemplazo: 0x0\n");
  } else {
    int to_be_replaced = 0;
    for (int i = 0; i < TLB_size; i++) {
      if (get_entry_last_access_iteration(i) < get_entry_last_access_iteration(to_be_replaced)) {
        to_be_replaced = i;
      }
    }
    printf("Politica de reemplazo: %p\n", (void*)TLB + (to_be_replaced * TLB_ENTRY_SIZE));
    set_entry_address(to_be_replaced, address);
    set_entry_page_number(to_be_replaced, page_number);
    set_entry_offset(to_be_replaced, offset);
    set_entry_page_binary(to_be_replaced, page_binary);
    set_entry_offset_binary(to_be_replaced, offset_binary);
    set_entry_last_access_iteration(to_be_replaced, last_access_iteration);
  }
}

// Función para convertir un número decimal a binario.
void decimal_to_binary(unsigned int decimal, char* binary, int bits) {
  for (int i = bits - 1; i >= 0; i--) {
      binary[i] = (decimal & 1) ? '1' : '0';
      decimal >>= 1;
  }
  binary[bits] = '\0';
}

// Función para convertir un número binario a decimal.
unsigned int binary_to_decimal(unsigned char* binary) {
  unsigned int decimal = 0;
  for (int i = 0; binary[i] != '\0'; i++) {
      if (binary[i] == '1') {
          decimal += (1 << (strlen(binary) - i - 1));
      }
  }
  return decimal;
}

// Función para obtener el tiempo actual en segundos.
double get_time() {
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return tv.tv_sec + tv.tv_usec / 1e6;
}

// Función para limpiar y liberar recursos.
void cleanup() {
  free_TLB();
}

// Función principal.
int main() {
  initialize_TLB();
  char input[20];
  unsigned int address;
  unsigned int current_iteration = 0;
  while (1) {
    current_iteration ++;
    printf("Ingrese dirección virtual: ");
    scanf("%s", input);

    if (input[0] == 's') {
      printf("Good bye!\n");
      break;
    }

    address = (unsigned int)atoi(input);
    if (!is_valid_address(address)) {
      printf("Page Fault\n");
      continue;
    }

    double start_time = get_time();
    
    unsigned int page_number = get_page_number(address);
    unsigned int offset = get_offset(address);
    
    char page_binary[21]; 
    char offset_binary[13];
    
    decimal_to_binary(page_number, page_binary, 20);
    decimal_to_binary(offset, offset_binary, 12);
    
    bool tlb_hit = false;
    for (int i = 0; i < TLB_size; i++) {
      if (get_entry_address(i) == address) {
        tlb_hit = true;
        break;
      }
    }

    printf("TLB desde %p hasta %p\n", (void*)TLB, (void*)(TLB + 5 * TLB_ENTRY_SIZE));
    if (tlb_hit) {
        printf("TLB Hit\n");
    } else {
        printf("TLB Miss\n");
    }
    printf("Página: %u\n", page_number);
    printf("Desplazamiento: %u\n", offset);
    printf("Página en binario: %s\n", page_binary);
    printf("Desplazamiento en binario: %s\n", offset_binary);
    if (tlb_hit){
      printf("Politica de reemplazo: 0x0\n");
    }else{
      add_to_TLB(address, page_number, offset, page_binary, offset_binary, current_iteration);
    }
    printf("Tiempo: %f segundos\n\n", get_time() - start_time);
  }

  cleanup();
  return 0;
}