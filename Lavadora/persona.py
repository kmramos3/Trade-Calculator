class Lavadora: 
    def __init__(self):
        pass    # Esto quiere dar a entender , de que nuestro constructor no tiene parametros


    def lavar (self, temperatura = 'fría'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar() 
        
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    
    def _anadir_jabon(self):
        print('Añadiendo jabón magía blanca')

    
    def _lavar(self):
        print('Lavando la ropa')


    def _centrifugar(self):
        print('Centrifugndo la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()