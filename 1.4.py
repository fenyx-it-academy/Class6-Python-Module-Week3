liste=int(input('sayi giriniz'))
def toplam(*liste):
    sum=0
    for n in liste:
       sum=sum+n
print(toplam(liste))  