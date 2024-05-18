from utilidades import *
from procesador import Procesador
from memoria import MemoriaPrincipal
from computador import Computador

alberto_cpu = Procesador(0, 0, 4)

# memoria_pruebas o False:
alberto_ram = MemoriaPrincipal("memoria_pruebas.txt")

alberto_computador = Computador(alberto_cpu, alberto_ram)
alberto_computador.ini_comp()

