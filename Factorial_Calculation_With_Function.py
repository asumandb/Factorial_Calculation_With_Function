def faktoriyel(n):
    if n < 0:
        return "Negatif sayıların faktöriyeli hesaplanamaz."

    elif n == 0 or n == 1:
        return 1 

    else:
        return n * faktoriyel(n - 1)

sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))
faktoriyel(sayi)
