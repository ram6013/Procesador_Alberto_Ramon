from utilidades import *

class MemoriaPrincipal:
    def __init__(self, datos):
        self.memoria = {}
        for direccion in range(2**16):
            self.memoria[dec_a_bin_16b(direccion)] = "0000000000000000"
        self.carg_mem_fich(datos)

    def g_mem_fich(self, fichero):
        f = open(fichero, "w")
        for direccion in self.memoria:
            f.write(direccion + "\t" + self.memoria[direccion] + "\n")
        f.close()

    def carg_mem_fich(self, fichero):
        try:
            f = open(fichero, "r")
            contenido = f.read().splitlines()
            f.close()
            for linea in contenido:
                valores_linea = linea.split("\t")
                direccion = valores_linea[0]
                valor = valores_linea[1]
                self.memoria[direccion] = valor
        except FileNotFoundError:
            print("No se encuentra {fichero}")

    def cont_dir_mem(self, direccion):
        return self.memoria[direccion]

    def escr_dir_mem(self, direccion, contenido):
        self.memoria[direccion] = contenido