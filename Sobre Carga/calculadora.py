# Calculadora
class Calculadora:
  global dato1 
  dato1= int(input("Ingrese el primer número: "))
  
  global dato2 
  dato2= int(input("Ingrese el segundo número: "))
  
  # Método Constructor 
  def _init_(self):
    pass
  
  def operaciones(self):
    self._suma()
    self._resta()
    self._multiplicacion()
    self._division()
  
  def _suma(self):
    suma = dato1 + dato2
    print(f"La suma entre {dato1} y {dato2} es: {suma}")

  def _resta(self):
    resta = dato1 - dato2
    print(f"La resta entre {dato1} y {dato2} es: {resta}")

  def _multiplicacion(self):
    multi = dato1 * dato2
    print(f"La multiplicación entre {dato1} y {dato2} es: {multi}")

  def _division(self):
    division = dato1 / dato2
    print(f"La división entre {dato1} y {dato2} es: {division}")

# Entry Point 
if __name__ == '__main__':
  calculadora = Calculadora()
  calculadora.operaciones()