class Movie:
    def __init__(self, title, hero, rating):
        self.title = title
        self.hero = hero
        self.rating = rating

    def display(self):
        print("Movie:", self.title)
        print("Hero:", self.hero)
        print("Rating:", self.rating)

m = Movie("RRR", "Ram Charan", 9)

m.display()