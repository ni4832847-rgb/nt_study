class Book:
    def __init__(self,book_id,title,author,category,total_stock,available_stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.total_stock = total_stock
        self.available_stock = available_stock


    def to_dict(self):
        return {
            "book_id":self.book_id,
            "title":self.title,
            "author":self.author,
            "category":self.category,
            "total_stock":self.total_stock,
            "available_stock":self.available_stock
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["category"],
            data["total_stock"],
            data["available_stock"],
        )
