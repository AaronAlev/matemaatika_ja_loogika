name = input("Sisestage oma nimi: ")
max_speed = input("Sisestage lubatud kiirus (hm/h): ")
actual_speed = input("Sisestage tegelik kiirus: ")
fine = (int(actual_speed) - int(max_speed)) * 3
fine = min(190, fine)

if fine > 0:
    print(f"{name}, kiiruse ületamise eest on teie trahv {fine} eurot.")
if fine <= 0:
    print(f"{name}, olete tubli liikleja.")
