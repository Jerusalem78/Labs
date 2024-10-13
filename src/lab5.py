# 1
class Book():
    title = 'Книга'
    author = 'Пушкин'
    year = 1999

    @classmethod
    def get_info(cls):
        return f"Название: {cls.title}\nАвтор: {cls.author}\nГод: {cls.year}"
    

Book.title = 'Name'
Book.author = 'auvtor'
Book.year = 34324

print(Book.get_info())


# 2
class Circle:
    def __init__(self, radious):
        self.radious = radious

    def get_radious(self):
        return self.radious
    
    def set_radious(self, new_radious):
        self.radious = new_radious
    

Obj = Circle(23)
Obj.set_radious(345)
print(Obj.get_radious())