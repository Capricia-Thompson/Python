class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self, ):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Active rewards member?: {self.is_rewards_member}")
        print(f"Gold points balance: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(
                f"Thanks for enrolling, {self.first_name}. New members get 200 points!")
            return True

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            print(
                f"You used {amount} points. You have {self.gold_card_points} points remaining.")
        else:
            print("Not enough points available for purchase.")


admin = User("Capricia", "Thompson", "thompsoncapricia@gmail.com", 31)

admin.display_info()
admin.enroll()

user2 = User("Jane", "Doe", "jdoe@gmail.com", 22)
user3 = User("John", "Smith", "smithj@gmail.com", 38)

admin.spend_points(50)
user2.enroll()
user2.spend_points(80)

admin.display_info()
user2.display_info()
user3.display_info()

admin.enroll()
user3.spend_points(40)
