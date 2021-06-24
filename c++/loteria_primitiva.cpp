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
  int numeros_ganadores[6];

  for (int i = 0; i < 6; i++) {
    cout << "Ingresa el numero ganador de la rifa primitiva" << endl;
    cin >> numeros_ganadores[i];
  } 

  sort(numeros_ganadores, 0, 5);

  cout << endl << "Numeros ordenados: " << endl;
  for (int i = 0; i < 6; i++) {
    cout << numeros_ganadores[i] << " "; 
  }

  return 0;
}