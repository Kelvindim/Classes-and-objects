class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, newname):
        self_name = newname
        print("My name is", self.name)

    def change_age(self, newage):
        self_age = newage
        print("And my age is", self.age)

    def add_tracks(self, tracks):
        self.tracks.append(tracks)
        print("I am offering tracks", self.tracks)

    def get_score(self):
        print("The score I got is", self.score)


Bob = Student(name="Peter", age=34, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()
