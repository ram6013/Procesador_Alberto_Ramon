from procesador import Procesador
from memoria import MemoriaPrincipal
from computador import Computador

try:
    alberto_cpu = Procesador(0, 0, 4)
    file = str(input("Proporcione el nombre de la memoria que quieres usar.\nEjemplo: memoria_pruebas.txt\n"))
    # memoria_pruebas o False:
    alberto_ram = MemoriaPrincipal(file)

    alberto_computador = Computador(alberto_cpu, alberto_ram)
    alberto_computador.ini_comp()
except ValueError as e:
    print(e)  
