presidenIndonesia   =   [
    'Soekarno', 'Soeharto', 'BJ. Habibie',
    'Abdurrahman Wahid', 'Megawati', 'SBY',
    'Jokowi'
]

president   =   presidenIndonesia

print(presidenIndonesia)
president.append('Falentino')
print(presidenIndonesia)

print(president)
presidenIndonesia.append('Eko')
print(president)

#Conclusion
#If you assign a new variable (president) with an already exist variable (presidenIndonesia)
#it won't change the value of president value cause it only reference to presidenIndonesia value, it will change presidenIndonesia value.  
#It can be happened cause you only make other name of presidenIndonesia (president), but actually the address is always same.

#But if you put a "[:]" it will copy whole its (presidenIndonesia) value to president variable, and it won't affect presidenIndonesia value if you try to manipulate president value
#cause you have copy its value to a new variable, not reference it to a new variable

#Addition note
#If you manipulate presidenIndonesia, it will affect to president value, and vice versa.