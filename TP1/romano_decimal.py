#Ejercicio Nº 5, Desarrolar una funcion que permita convertir un nùmero romano a un nùmero decimal.
def romano_a_decimal(romano_numeral):
    romano_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decimal_num = 0
    pre_num = 0
    for char in romano_numeral[::-1]:
        curr_num = romano_dict[char]
        if curr_num < pre_num:
            decimal_num -= curr_num
        else:
            decimal_num += curr_num
        pre_num = curr_num
    return decimal_num

num_romano = "MIL"
num_decimal = romano_a_decimal(num_romano)
print(f"El número romano {num_romano} es el número decimal {num_decimal}")
