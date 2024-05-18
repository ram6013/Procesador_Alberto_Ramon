from utilidades import *

class Procesador:
    def __init__(self, pc, ir, num_registros):
        self.pc_reg = dec_a_bin_16b(pc)
        self.ir_reg = ir
        self.registros = {}
        for i in range(num_registros):
            self.registros[dec_a_bin_16b(i)] = "0000000000000000"

    def get_pc(self):
        return self.pc_reg

    def set_pc(self, pc):
        self.pc_reg = pc

    def get_ir(self):
        return self.ir_reg

    def set_ir(self, ir):
        self.ir_reg = ir

    def get_reg(self, registro):
        return self.registros[registro]

    def set_reg(self, registro, valor):
        self.registros[registro] = valor

    def most_reg_proc(self):
        print("Registros del procesador:")
        for registro in self.registros:
            print(f"{registro}: {self.registros[registro]}")

    def ejec_inst(self, memoria):
        op_code = self.ir_reg[:4]

        # LOAD target, source
        if op_code == "0000":
            target = bin_a_dec(self.ir_reg[4:16])
            registro = dec_a_bin_16b(target)
            source = self.ir_reg[16:]
            self.set_reg(registro, source)
            # contenido_memoria = memoria.cont_dir_mem(source)
            # self.set_reg(registro, contenido_memoria)
        # LOADI target, source
        elif op_code == "0001":
            target = bin_a_dec(self.ir_reg[4:16])
            registro = dec_a_bin_16b(target)
            source = self.ir_reg[16:]
            self.set_reg(registro, source)

        # SWAP source1, source2
        elif op_code == "0010":
            source1 = bin_a_dec(self.ir_reg[4:10]) 
            registro1 = dec_a_bin_16b(source1)
            registro2 = self.ir_reg[16:]
            aux = self.get_reg(registro1)
            self.set_reg(registro1, self.get_reg(registro2)) 
            self.set_reg(registro2, aux)

        # STORE target, source
        elif op_code == "0011":
            target = bin_a_dec(self.ir_reg[4:16])
            direccion_memoria = dec_a_bin_16b(target)
            contenido = self.get_reg(self.ir_reg[16:])
            memoria.escr_dir_mem(direccion_memoria, contenido)

        # STOREI target, source
        elif op_code == "0100":
            target = bin_a_dec(self.ir_reg[4:16])
            direccion_memoria = dec_a_bin_16b(target)
            contenido = self.ir_reg[16:]

        # ADD target, source
        elif op_code == "0101":
            target = bin_a_dec(self.ir_reg[4:16]) 
            print("Soy target: " + str(target)) 
            registro1 = dec_a_bin_16b(target)
            print("hola soy esto " + str(registro1))
            registro2 = self.ir_reg[16:]
            cont_r1 = self.get_reg(registro1)
            cont_r2 = self.get_reg(registro2)
            resultado_suma = bin_a_dec(cont_r1) + bin_a_dec(cont_r2)
            self.set_reg(registro1, dec_a_bin_16b(resultado_suma))

        # ADDI target, source 
        elif op_code == "0110":
            target = bin_a_dec(self.ir_reg[4:16])
            registro = dec_a_bin_16b(target)
            valor = self.ir_reg[16:]
            cont_reg = self.get_reg(registro)
            resultado_suma = bin_a_dec(cont_reg) + bin_a_dec(valor)
            self.set_reg(registro, dec_a_bin_16b(resultado_suma))

        # SUB target, source
        elif op_code == "0111":
            target = bin_a_dec(self.ir_reg[4:16])
            registro1 = dec_a_bin_16b(target)
            registro2 = self.ir_reg[16:]
            cont_r1 = self.get_reg(registro1)
            cont_r2 = self.get_reg(registro2)
            resultado_resta = bin_a_dec(cont_r1) - bin_a_dec(cont_r2)
            if resultado_resta < 0:
                print ("ERROR! Nuestro sistema no permite trabajar con numeros negativos")
            self.set_reg(registro1, dec_a_bin_16b(resultado_resta))

        # SUBI target, source
        elif op_code == "1000":
            target = bin_a_dec(self.ir_reg[4:16])
            registro = dec_a_bin_16b(target)
            valor = self.ir_reg[16:]
            cont_reg = self.get_reg(registro)
            resultado_resta = bin_a_dec(cont_reg) - bin_a_dec
            if resultado_resta < 0:
                print ("ERROR! Nuestro sistema no permite trabajar con numeros negativos")
            self.set_reg(registro, dec_a_bin_16b(resultado_resta))

        # INC target
        elif op_code == "1001":
            target = bin_a_dec(self.ir_reg[4:16])
            registro = dec_a_bin_16b(target)
            cont_reg = bin_a_dec(self.get_reg(registro))
            self.set_reg(registro, dec_a_bin_16b(cont_reg + 1))

        # DEC target
        elif op_code == "1010":
            target = bin_a_dec(self.ir_reg[4:16])
            registro = dec_a_bin_16b(target)
            cont_reg = bin_a_dec(self.get_reg(registro))
            if cont_reg == 0:
                print("ERROR! No se puede decrementar un registro con valor 0")
            else:
                self.set_reg(registro, dec_a_bin_16b(cont_reg - 1))

        # JMP target
        elif op_code == "1011":
            target = bin_a_dec(self.ir_reg[4:20])
            print("target : " + str(target))
            direccion_memoria = dec_a_bin_16b(target)
            print("pasamos a pc: " + str(direccion_memoria))
            self.set_pc(direccion_memoria)

        # JMPC target, source1, source2
        elif op_code == "1100":
            print("setIR; "+ str(self.ir_reg[4:16]))
            target = bin_a_dec(self.ir_reg[4:16])
            direccion_memoria = dec_a_bin_16b(target)
            source1 = bin_a_dec(self.ir_reg[16:22])
            registro1 = dec_a_bin_16b(source1)
            source2 = self.ir_reg[22:]
            registro2 = dec_a_bin_16b(bin_a_dec(self.ir_reg[22:]))
            if self.get_reg(registro1) != self.get_reg(registro2):
                self.set_pc(direccion_memoria)