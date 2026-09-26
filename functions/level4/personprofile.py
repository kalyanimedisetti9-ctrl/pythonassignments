def profile(**kwargs):
    print("Person Profile:")

    for key, value in kwargs.items():
        print(key, ":", value)

profile(
    name="Kalyani",
    age=18,
    city="Rajahmundry",
    profession="Student"
)