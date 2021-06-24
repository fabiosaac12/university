#include<iostream>
#include<stdlib.h>
using namespace std;

int main () {
  int notas[2];

  while (true) {
    cout << "Ingresa la nota de Programacion II" << endl;
    cin >> notas[0];
    
    cout << "Ingresa la nota de Estructura de Datos" << endl;
    cin >> notas[1];

    if (((notas[0] + notas[1]) / 2) >= 10) {
      cout << endl << "El alumno ha aprobado." << endl;
    } else {
      cout << endl << "El alumno ha reprobado. Esta fuera de la universidad." << endl;
    }

    system("cls");
  }
  
  return 0;
}