class Nodo(object):
    info, sig = None, None


class datoPolinomio(object):

    def init(self, valor, termino):
        self.valor = valor
        self.termino = termino


class Polinomio(object):

    def __init__(self):
        '''
        Vamos a guardar en el objeto un diccionario con los elementos con clave el grado, por ejemplo:
        {3: 1, 2: 3} sería x3 + 3x2. Por ejemplo {3:2, 0:1} sería 2x3 + 1 (ya que x^0 es la unidad)
        :return:
        '''
        self.grado_mayor = 0
        self.contenido = {}

    def agregar_termino(self, grado, valor):
        '''
        Agregamos un término, que es meter un elemento en el diccionario con clave el grado y valor el valor del término
        :param grado:
        :param valor:
        :return:
        '''
        self.contenido[grado] = valor
        if self.grado_mayor < grado:
            self.grado_mayor = grado

    def obtener_valor(self, grado):
        '''
        retornamos el valor del grado, ojo que puede devolver None si no hay ese grado
        :param grado:
        :return:
        '''
        return self.contenido[int(grado)]

    def restar(self, polinomio1, polinomio2):
        menor = polinomio1 if (polinomio1.grado_mayor < polinomio2.grado_mayor) else polinomio2
        mayor = polinomio2 if (menor == polinomio1) else polinomio1
        self.contenido = mayor.contenido
        for i in range(0, menor.grado_mayor + 1):
            try:
                mayor_valor = 0 if mayor.existe_grado(i) is False else mayor.obtener_valor(i)
                menor_valor = 0 if menor.existe_grado(i) is False else menor.obtener_valor(i)
                total = mayor_valor - menor_valor
                if self.existe_grado(i) :
                    self.elimina_grado(i)
                if total != 0:
                    self.agregar_termino(i, total)
            except:
                self.agregar_termino(i, total)
                pass

    def elimina_grado(self, grado):
        '''
        elimina el elemento del diccionario
        :param grado:
        :return:
        '''
        del self.contenido[grado]
        if grado == self.grado_mayor:
            self.grado_mayor = max(self.contenido.keys())

    def existe_grado(self, grado):
        '''
        retorna true si existe o false si no existe
        :param grado:
        :return:
        '''
        try:
            return self.contenido[grado] is not None
        except:
            return False


    def existe_termino(self, termino):
        '''
        returna True si coinciden el grado y el ter
        :param grado:
        :param valor:
        :return:
        '''
        valor = 1 if termino.split('x')[0] == '' else int(termino.split('x')[0])
        grado = 1 if termino.split('x')[1] == '' else int(termino.split('x')[1])
        try:
            valor_obtenido = self.contenido[grado]
            if valor_obtenido == valor:
                return True
            else:
                return False
        except Exception as e:
            print(f'Error {repr(e)}')
            return False

    def __str__(self):
        return_str = ''
        ordenado = dict(sorted(self.contenido.items(), reverse=True))
        for i in ordenado.keys():
            grado = '' if i == 1 else i
            valor = '' if ordenado[i]==1 else ordenado[i]
            return_str = return_str + f'{valor}x{grado} '
        return return_str


if __name__ == '__main__':
    poli = Polinomio()
    poli.agregar_termino(2, 3)  # esto mete un 3x2
    poli.agregar_termino(0, -1)  # esto mete un -1
    # ahora poli es 3x2 - 1
    print(poli)
    print(poli.contenido)
    # debería ser {2:3, 0:1}
    print(poli.grado_mayor)
    # debería ser 2
    grado_test = 2
    print(f'Existe el grado {grado_test}? :{poli.existe_grado(grado_test)}')
    termino = '3x2'
    print(f'Existe el termino {termino}? :{poli.existe_termino(termino)} ')

    # Test resta (3x2 - 1) - (2x - 1) = 3x2 - 2x
    poli1 = Polinomio()
    poli1.agregar_termino(2, 3)
    poli1.agregar_termino(0, -1)
    poli2 = Polinomio()
    poli2.agregar_termino(1, 2)
    poli2.agregar_termino(0, -1)
    resultado = Polinomio()
    resultado.restar(poli1, poli2)
    print(resultado)