from diaries.DiarySample import DiarySample
from diaries.KaneiwaDiary import DiarySample
from diaries.KannouDiary import KannouDiary
from diaries.NomuraDiary import DiarySample
from diaries.ShutoDiary import ShutoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           DiarySample(), 
           KannouDiary(), 
           DiarySample(), 
           ShutoDiary(), ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()