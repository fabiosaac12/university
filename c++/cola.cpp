#include<iostream>
using namespace std;

class Cola {
  public:
    int numero_elementos = 0;
    int max = 10;
    int arreglo[10];
    int primer_elemento = -1;
    int ultimo_elemento = -1;
    
    void encolar(int elemento) {
      if (numero_elementos < max) {
        if (ultimo_elemento + 1 < max) {
          ultimo_elemento ++;
        } else {
          ultimo_elemento -= max - 1;
        }

        arreglo[ultimo_elemento] = elemento;

        if (primer_elemento < 0) {
          primer_elemento = 0;
        }

        numero_elementos ++;
      }
    }

    void desencolar() {
      if (numero_elementos > 0) {
        primer_elemento ++;
        numero_elementos --;
      }
    }

    void mostrar() {
      int i = primer_elemento;
      
      while (i != ultimo_elemento) {
        cout << arreglo[i] << " ";
        
        if (i + 1 < max) {
          i++;
        } else {
          i = 0;
        }
      }
        
      cout << arreglo[i] << endl;
    }

    int obtener(int posicion) {
      if (posicion < numero_elementos) {
        if (primer_elemento + posicion < max) {
          return arreglo[primer_elemento + posicion];
        } else {
          return arreglo[primer_elemento + posicion - max];
        }
      } else {
        return 0;
      }
    }

    bool vacia() {
      return numero_elementos == 0;
    }

    bool llena() {
      return numero_elementos == max;
    }
};

Cola interseccion(Cola cola1, Cola cola2) {
  Cola cola;

  while (!cola1.vacia() && !cola2.vacia()) {
    int primer_elemento_cola1 = cola1.obtener(0);
    int primer_elemento_cola2 = cola2.obtener(0);

    if (primer_elemento_cola1 == primer_elemento_cola2) {
      cola.encolar(primer_elemento_cola1);

      cola1.desencolar();
      cola2.desencolar();
    } else {
      if (primer_elemento_cola1 < primer_elemento_cola2) {
        cola1.desencolar();
      } else {
        cola2.desencolar();
      }
    }
  }
  
  return cola;
}

int main() {
  Cola cola1;
  Cola cola2;

  cola1.encolar(10);
  cola1.encolar(30);
  cola1.encolar(4);
  cola1.encolar(12);
  cola1.encolar(1);
  cola1.encolar(3);
  cola1.encolar(4);
  cola1.encolar(6);
  cola1.encolar(8);
  cola1.encolar(11);
  cola1.desencolar();
  cola1.desencolar();
  cola1.desencolar();
  cola1.desencolar();
  
  cola2.encolar(1);
  cola2.encolar(4);
  cola2.encolar(5);
  cola2.encolar(9);
  cola2.encolar(10);
  cola2.encolar(11);

  cola1.mostrar();
  cola2.mostrar();

  Cola cola_interseccion = interseccion(cola1, cola2);

  cola_interseccion.mostrar();
  
  return 0;
}
