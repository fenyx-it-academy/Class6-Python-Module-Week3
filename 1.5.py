num=int(input('sayilari girin'))
liste=num.split(' ')
def adder(liste):
    if len(liste)>=5:
        return ('Besten uzun')
    elif len(liste)<5:
        return('Besten az')   
adder(liste) 