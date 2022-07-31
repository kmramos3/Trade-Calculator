import os  # Libreria para limpiar la consola

class Persona: 

    def __init__(self):
        pass   # Esto indica que no recibe ningún parametro


    def formulario(self):
        self._pedir_nombre()
        self._pedir_apellidos()
        self._pedir_dpi()
        self._peso_persona()
        self._año_nacimiento()

    
    def _pedir_nombre(self):
        global nombre
        nombre = input('Registra tu nombre: ')
        print(f'Nombre {nombre} registrado.')


    def _pedir_apellidos(self):
        global apellidos
        apellidos = input('Registre sus apellidos: ')
        print(f'Apellido {apellidos} registrado.')


    def _pedir_dpi(self):
        global dpi
        dpi = input('Ingrese su DPI: ')
        print('DPI **** ***** **** registrado exitosamente.')


    def _peso_persona(self):
        global pesokg 
        pesokg = int(input('Ingrese su peso en kg: '))
        print(f'Peso de {pesokg}kg. agregado.')


    def _año_nacimiento(self):
        global nacimiento
        nacimiento = int(input('Ingrese su año de nacimiento: '))
        self._limpiar_consola()

    
    def _limpiar_consola(self):
        if (os.name == 'nt'):
            os.system("cls")
            self._mostrar_datos()
        else: 
            os.system("clear")
            self._mostrar_datos()

        
    def _mostrar_datos(self):
        print(f'Nombre: {nombre}')
        print(f'Apellidos: {apellidos}')
        print(f'No. DPI: {dpi}')
        print(f'Año de nacimiento: {nacimiento}')

        # Conversión edad
        año = 2022
        edad = año - nacimiento
        print(f'su edad es: {edad} años')
        print(f'Su peso en kg es de: {pesokg}kg.')

        # Conversión a libras
        pesolbs = pesokg * 2.205
        print(f'Su peso en lbs es: {pesolbs}lbs.')
        

# Entriy Point
if __name__ == '__main__':
    persona = Persona()
    persona.formulario()