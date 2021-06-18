#include <iostream>
using namespace std;

void sort(int arr[], int inicio, int fin) {
  if (inicio < fin) {
    int pivote = arr[inicio];

    int i = inicio + 1;

    for (int j = i; j <= fin; j++) {
      if (arr[j] < pivote) {
        int valorEnLaPosicionJ = arr[j];
        int valorEnLaPosicionI = arr[i];
        arr[i] = valorEnLaPosicionJ;
        arr[j] = valorEnLaPosicionI;
        i++;
      }
    }

    arr[inicio] = arr[i-1];
    arr[i-1] = pivote;

    int posicion_pivote = i - 1;
    
    sort(arr, inicio, posicion_pivote - 1);
    sort(arr, posicion_pivote + 1, fin);
  }
}

int main() {
  int arreglo[] = {140, 10, 5, 9, 16, 8, 0, 1, 52};

  cout << "Arreglo desordenado: ";
  for (int i = 0; i <= 8; i++) {
    cout << arreglo[i] << " "; 
  }
  cout << endl;

  sort(arreglo, 0, 8);

  cout << "Arreglo ordenado: ";
  for (int i = 0; i <= 8; i++) {
    cout << arreglo[i] << " "; 
  }

  return 0;
}