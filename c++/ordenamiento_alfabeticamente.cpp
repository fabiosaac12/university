#include<iostream>
using namespace std;

void sort(string arr[], int inicio, int fin) {
  if (inicio < fin) {
    string pivote = arr[inicio];

    int i = inicio + 1;

    for (int j = i; j <= fin; j++) {
      if (arr[j] < pivote) {
        string valorEnLaPosicionJ = arr[j];
        string valorEnLaPosicionI = arr[i];
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
  int arreglo[] = {"b", "f", "g", "c", "a", "e", "h", "d", "i"};

  sort(arreglo);

  cout << "Arreglo ordenado: ";
  for (int i = 0; i <= 8; i++) {
    cout << arreglo[i] << " "; 
  }

  return 0;
}