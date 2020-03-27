import unittest
import psp0

class PSP0TestCase(unittest.TestCase):

    def test_construir(self):
        esperado = (1, None)
        observado = psp0.construir(1)
        self.assertEqual(esperado, observado)

        esperado = (1.5, None)
        observado = psp0.construir(1.5)
        self.assertEqual(esperado, observado)

        esperado = (1, (2, None))
        observado = psp0.construir(1, psp0.construir(2))
        self.assertEqual(esperado, observado)

        self.assertRaises(ValueError, psp0.construir, "a")

    def test_lista(self):
        esperado = None
        observado = psp0.lista()
        self.assertEqual(esperado, observado)

        esperado = (1, None)
        observado = psp0.lista(1)
        self.assertEqual(esperado, observado)
        
        esperado = (1, (2, None))
        observado = psp0.lista(1, 2)
        self.assertEqual(esperado, observado)
        
    def test_primero(self):
        l = psp0.lista(1, 2, 3)
        esperado = 1
        observado = psp0.primero(l)
        self.assertEqual(esperado, observado)

    def test_resto(self):
        l = psp0.lista(1, 2, 3)
        esperado = psp0.lista(2, 3)
        observado = psp0.resto(l)
        self.assertEqual(esperado, observado)

    def test_vacia(self):
        l = psp0.lista()
        esperado = True
        observado = psp0.vacia(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(1)
        esperado = False
        observado = psp0.vacia(l)
        self.assertEqual(esperado, observado)

    def test_largo(self):
        l = psp0.lista()
        esperado = 0
        observado = psp0.largo(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(1, 2, 3)
        esperado = 3
        observado = psp0.largo(l)
        self.assertEqual(esperado, observado)

    def test_sumar(self):
        l = psp0.lista()
        esperado = 0
        observado = psp0.sumar(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(1, 2, 3)
        esperado = 6
        observado = psp0.sumar(l)
        self.assertEqual(esperado, observado)

    def test_mapear(self):
        l = psp0.lista(1, 2, 3)
        esperado = psp0.lista(1, 4, 9)
        observado = psp0.mapear(lambda x: x * x, l)
        self.assertEqual(esperado, observado)

        esperado = psp0.lista(0, 1, 2)
        observado = psp0.mapear(lambda x: x - 1, l)
        self.assertEqual(esperado, observado)

    def test_promedio(self):
        l = psp0.lista()
        esperado = 0
        observado = psp0.promedio(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(5)
        esperado = 5
        observado = psp0.promedio(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(1, 1.5)
        esperado = 1.25
        observado = psp0.promedio(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
        esperado = 638.9
        observado = psp0.promedio(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503)
        esperado = 550.6
        observado = psp0.promedio(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)
        esperado = 60.31999999999999
        observado = psp0.promedio(l)
        self.assertEqual(esperado, observado)

    def test_desviacion(self):
        l = psp0.lista()
        esperado = 0
        observado = psp0.desviacion(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(5)
        esperado = 0
        observado = psp0.desviacion(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
        esperado = 625.6339806770231
        observado = psp0.desviacion(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503)
        esperado = 572.0268447469149
        observado = psp0.desviacion(l)
        self.assertEqual(esperado, observado)

        l = psp0.lista(15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)
        esperado = 62.25583060601187
        observado = psp0.desviacion(l)
        self.assertEqual(esperado, observado)
