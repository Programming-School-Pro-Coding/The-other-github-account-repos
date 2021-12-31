class The_Born:
    def __init__(self, name, date_of_birthday, the_date_of_now=""):
        self.name = name
        self.date_of_birthday = date_of_birthday
        self.the_date_of_now = the_date_of_now
    

    def display(self):
        return f"Your name is {self.name} and your birthday is {self.date_of_birthday}, and your age is {self.the_date_of_now}"


born1 = The_Born("Mohamed", "9/9/2009", "4/11/2021")

