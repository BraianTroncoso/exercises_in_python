"""TABLAS DE LA VERDAD"""


# AND -> True, False
# SIEMPRE QUE AMBAS CONDICIONES SEAN TRUE DEVUELVE TRUE, DE LO CONTRARIO FALSE
print("t y t", True and True)
print("t y f", True and False)
print("f y f", False and False)
print("f y t", False and True)
print("f y f", False and False)

# OR -> True, False
# SIEMPRE QUE UNA DE LAS DOS CONDICIONES SEAN CIERTAS DEVOLVERA TRUE
# PARA QUE SEA FALSA POR ENDE AMBAS NO SE TIENEN QUE CUMPLIR
print("t o t", True or True)
print("t o f", True or False)
print("f o f", False or False)
print("f o t", False or True)
print("f o f", False or False)

# XOR -> True, False
# PARA QUE XOR SEA CIERTO UNO DE LOS DOS TIENEN QUE SER FALSOS
print("t xor t", True ^ True)
print("t xor f", True ^ False)
print("f xor f", False ^ False)
print("f xor t", False ^ True)
print("f xor f", False ^ False)
