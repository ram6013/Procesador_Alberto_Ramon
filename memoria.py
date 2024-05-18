from utilidades import *

class MemoriaPrincipal:
    def __init__(self, datos):
        self.memoria = {dec_a_bin_16b(direccion): "0000000000000000" for direccion in range(2**16)}
        if not self.carg_mem_fich(datos):
            raise ValueError(f"No se pudo cargar la memoria desde el archivo: {datos}")

    def g_mem_fich(self, fichero):
        with open(fichero, "w") as f:
            for direccion in self.memoria:
                f.write(direccion + "\t" + self.memoria[direccion] + "\n")

    def carg_mem_fich(self, fichero):
        try:
            with open(fichero, "r") as f:
                contenido = f.read().splitlines()
            for linea in contenido:
                valores_linea = linea.split("\t")
                direccion = valores_linea[0]
                valor = valores_linea[1]
                self.memoria[direccion] = valor
            return True
        except FileNotFoundError:
            print(f"No se encuentra el archivo {fichero}.")
            return False
        except Exception as e:
            print(f"Error al cargar el archivo {fichero}: {e}.")
            return False

    def cont_dir_mem(self, direccion):
        return self.memoria[direccion]

    def escr_dir_mem(self, direccion, contenido):
        self.memoria[direccion] = contenido
