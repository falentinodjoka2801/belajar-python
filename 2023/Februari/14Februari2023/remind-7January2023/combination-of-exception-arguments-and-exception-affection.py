class Profesi(Exception):
    pass

class BidangKreatif(Profesi):
    pass

class BidangNonKreatif(Profesi):
    pass

class Programmer(BidangKreatif):
    pass

class Desainer(BidangKreatif):
    pass

class ContentCreator(BidangKreatif):
    pass

class Pedagang(BidangNonKreatif):
    pass

class Kurir(BidangNonKreatif):
    pass

class PetugasKebersihan(BidangNonKreatif):
    pass

programmer  =   Programmer('Web', 'Mobile', 'Desktop')
desainer    =   Desainer('Video', 'Foto')
content_creator =   ContentCreator('Youtuber', 'Selebgram')
pedagang    =   Pedagang('Makanan', 'Paket dan Pulsa', 'Alat Bangunan')
kurir   =   Kurir('JNE', 'JNT', 'TiKi')
petugas_kebersihan  =   PetugasKebersihan('PT. Indaco Indah Sejahtera', 'PT. Abab', 'PT. Cleaning')
bidang_kreatif  =   BidangKreatif(Programmer, Desainer, ContentCreator)
bidang_non_kreatif  =   BidangNonKreatif(Pedagang, Kurir, PetugasKebersihan)
profesi =   Profesi(BidangKreatif, BidangNonKreatif)

arguments   =   []
for profesi_item in [programmer, desainer, content_creator, pedagang, kurir, petugas_kebersihan, bidang_kreatif, bidang_non_kreatif, profesi]:
    
    try:
        raise profesi_item
    
    except Programmer as e:
        print('Programmer')
        arguments   =   e.args
    except Desainer as e:
        print('Desainer')
        arguments   =   e.args
    except ContentCreator as e:
        print('Content Creator')
        arguments   =   e.args
    except Pedagang as e:
        print('Pedagang')
        arguments   =   e.args
    except Kurir as e:
        print('Kurir')
        arguments   =   e.args
    except PetugasKebersihan as e:
        print('Petugas Kebersihan')
        arguments   =   e.args
    except BidangKreatif as e:
        print('Bidang Kreatif')
        arguments   =   e.args
    except BidangNonKreatif as e:
        print('Bidang Non Kreatif')
        arguments   =   e.args
    except Profesi as e:
        print('Profesi')
        arguments   =   e.args
    
    print('-------------------')
    for arg in arguments:
        if type(arg) != str:
            if issubclass(arg, Exception):
                print(arg.__name__)
                print('This is an exception')
        else:
            print('-')