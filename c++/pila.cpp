#include<iostream>
using namespace std;

class Pila {
  public:
    int numero_elementos = 0;
    int max = 10;
    int arreglo[10];

    void apilar(int elemento) {
      arreglo[numero_elementos] = elemento;
      numero_elementos ++;
    }

    void desapilar() {
      numero_elementos --;
    }

    void mostrar() {
      for (int i = 0; i < numero_elementos; i++) {
        cout << arreglo[i] << " "; 
      }
    }

    bool vacia() {
      return numero_elementos == 0;
    }

    bool llena() {
      return numero_elementos == 10;
    }
};

int main() {
  Pila pila;
  
  pila.apilar(2);
  pila.apilar(1);
  pila.apilar(3);
  pila.apilar(5);
  pila.apilar(5);
  pila.apilar(6);
  
  pila.mostrar();
  
  cout << endl << endl;
  
  pila.desapilar();
  pila.desapilar();
  pila.desapilar();
  
  pila.mostrar();
  
  cout << endl << endl;
  
  if (pila.vacia()) {
    cout << "Pila vacia"; 
  } else if (pila.llena()) {
    cout << "Pila vacia";
  } else {
    cout << "Pila ni vacia ni llena";
  }
  
  return 0;
}