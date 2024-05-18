def dec_a_bin(numero):
    return bin(numero).replace("0b","")

def dec_a_bin_16b(numero):
    binario = bin(numero).replace("0b", "")
    return  "0"*(16-len(binario)) + binario

def bin_a_dec(numero_binario):
    return int(numero_binario, 2)