#Ejercicio Nº 5, Desarrolar una funcion que permita convertir un nùmero romano a un nùmero decimal.
def romano_a_decimal(roman_numeral):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decimal_num = 0
    prev_num = 0
    for char in roman_numeral[::-1]:
        curr_num = roman_dict[char]
        if curr_num < prev_num:
            decimal_num -= curr_num
        else:
            decimal_num += curr_num
        prev_num = curr_num
    return decimal_num

num_romano = "IIV"
num_decimal = romano_a_decimal(num_romano)
print(f"El número romano {num_romano} es el número decimal {num_decimal}")
