from diaries.DiarySample import DiarySample
from diaries.KaneiwaDiary import KaneiwaDiary
from diaries.KannouDiary import KannouDiary
from diaries.NomuraDiary import NomuraDiary
from diaries.ShutoDiary import ShutoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           KaneiwaDiary(), 
           KannouDiary(), 
           NomuraDiary(), 
           ShutoDiary(), ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()