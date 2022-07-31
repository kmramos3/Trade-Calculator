import math

class Circulo:
  global diametro
  diametro = float(input("Ingresa el diámetro del círculo: "))

  def conversiones(self):
    self._radio()
    self._circunferencia()
    
  
  def _radio(sefl):
    radio = diametro / 2
    print(f"El radio de la circunferencia es: {radio}")
    
  
  def _circunferencia(self):
    circunferencia = diametro * math.pi
    print(f"La circunferencia del diámetro es de: {circunferencia}")

if __name__ == '__main__':
  circulo = Circulo()
  circulo.conversiones()