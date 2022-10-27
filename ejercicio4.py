
class Polinomio(object):

    def _init_(self):

        '''
        Vamos a guardar en el objeto un diccionario con los elementos con clave el grado, por ejemplo:
        {3: 1, 2: 3} sería x3 + 3x2. Por ejemplo {3:2, 0:1} sería 2x3 + 1 (ya que x^0 es la unidad)
        :return:
        '''
        
        self.grado_mayor = None
        self.contenido  = {}

    def agregar_termino(self, grado, valor):
        '''
        Agregamos un término, que es meter un elemento en el diccionario con clave el grado y valor el valor del término
        :param grado:
        :param valor:
        :return:
        '''
        self.contenido[grado] = valor
        if self.grado_mayor<grado:
            self.grado_mayor=grado


    def obtener_valor(self, grado):
        '''
        retornamos el valor del grado, ojo que puede devolver None si no hay ese grado
        :param grado:
        :return:
        '''
        return self.contenido[grado]

    def restar(self, polinomio1, polinomio2):
        menor = polinomio1 if (polinomio1.grado < polinomio2.grado) else polinomio2
        mayor = polinomio2 if (menor == polinomio1) else polinomio1
        self.contenido = mayor.conenido
        for i in range(0, menor.grado + 1):
            try:
                total = mayor.obtener_valor(i) - menor.obtener_valor(i)
                if total  != 0:
                    self.agregar_termino(i, total)
            except:
                pass


    def elimina_grado(self, grado):
        '''
        elimina el elemento del diccionario
        :param grado:
        :return:
        '''
        del self.contenido[grado]


    def existe_grado(self, grado):
        '''
        retorna true si existe o false si no existe
        :param grado:
        :return:
        '''
        return self.contenido[grado] is not None
