class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

# for cls in [D, C, B]:
#     try:
#         raise cls
#     except B:
#         print('B')
#     except C:
#         print('C')
#     except D:
#         print('D')

for cls in [B, C, D]:
    try:
        raise cls
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')

#14 Februari 2023 20:33 WIB
#Intinya, jika suatu kelas *mewarisi* suatu kelas, katakan B mewarisi A, maka exception kelas B adalah exception dari kelas induknya juga, yaitu kelas A.