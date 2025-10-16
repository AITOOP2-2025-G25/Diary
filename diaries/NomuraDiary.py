from diaries.AbstractDiary import AbstractDiary
class DiarySample(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "GItややこしい。あと、リーダーの負担が重い!"
    
    def get_author(self):
        return "Nomura"