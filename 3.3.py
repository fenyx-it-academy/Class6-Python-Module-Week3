def sphere():


    def sphere_area(r=int(input('Alan icin yaricap giriniz: '))):
        pi=3.14
        hesap1=(pi * (r ** 2))
        return hesap1
    def sphere_volume(r=int(input('Hacim icin yaricap giriniz: '))):
        pi=3.14
        hesap2=((4 / 3) * pi * (r ** 3))
        return hesap2

    print('alan: ', sphere_area())
    print('hacim: ', sphere_volume())

print(sphere())


