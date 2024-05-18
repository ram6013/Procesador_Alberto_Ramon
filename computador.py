from utilidades import *
import time
import sys
class Computador:
    
    def __init__(self, procesador, memoria):
        self.procesador = procesador
        self.memoria = memoria

    def ini_comp(self):

        contador_instruccion = 0

        while True:
                
                print("####################################")
                print(f"# Instruccion {contador_instruccion}")
                self.procesador.most_reg_proc()
                pc = self.procesador.get_pc()
                pc = bin_a_dec(pc)
                pc = dec_a_bin_16b(pc)
                instruccion = self.memoria.cont_dir_mem(pc)
                print(f"# Instruccion a ejecutar: {instruccion}")
                print("####################################")
                print(instruccion)
                self.procesador.set_ir(instruccion)
                print(instruccion)
                if instruccion[0:4] == "1111":
                    self.memoria.g_mem_fich("resultado.txt")
                    sys.exit(0)
                self.procesador.ejec_inst(self.memoria)
                if instruccion[0:4] != "1011" and instruccion [0:4] != "1100":
                    pc = bin_a_dec(pc) + 1
                    self.procesador.set_pc(dec_a_bin_16b(pc))
                contador_instruccion += 1
                time.sleep(0.5)
