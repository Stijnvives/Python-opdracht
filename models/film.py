class Film:
    def __init__(self, id, title, year, genre):
        self.id = id
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.id} | {self.title} | {self.year} | {self.genre}"
