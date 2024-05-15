# mehmonlar = ['Ali', 'Vali', 'G\'ani', 'Anvar', 'Islom', 'Mansur']
#
# for mehmon in mehmonlar:
#     print("Salom", mehmon)

# sonlar = list(range(1,11))
#
# for son in sonlar:
#     print(f"{son}ning kvadrati, {son**2} ga teng.")

# sonlar = list(range(2,11))
# kvadrat = []
#
# for son in sonlar:
#     kvadrat.append(son**2)
# print(sonlar)
# print(kvadrat)

# ismlar = ['Ali', 'Vali', 'G\'ani', 'Anvar', 'Islom', 'Mansur']
# sanoq = 0
#
# for ism in ismlar:
#     print("Salom", ism)
#     sanoq +=1
# print(f"kod {sanoq} takrorlandi")

# numbers = list(range(10,101))
#
# for odd in numbers:
#     if odd %2 != 0:
#         print(odd**3)

# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
#Natijani konsolga chiqaring.

# favourite_movies = []
# print("Name your Top 5 favourite Movies")
# for n in range(5):
#     favourite_movies.append((input(f"Write your {n+1} favourite movie? ")))
# print(favourite_movies)

# meeting = []
# person_met = int(input("How many people have you met today? "))
# person = 0
# for i in range(person_met):
#     person +=1
#     if person == 1:
#         added = 'st'
#     elif person == 2:
#         added = 'nd'
#     else:
#         added = 'th'
#     meeting.append(input(f"My {person}{added} talked person is: "))
#
# print(meeting)

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)


# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())



# javob = float(input("12x6 = ? : "))
# if javob != 72:
#     print("fuck u idiot")