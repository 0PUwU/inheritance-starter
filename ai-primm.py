class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def think(self):
        print("The human is thinking deeply.")

    def communicate(self):
        print("The human is communicating clearly.")

class AI(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        super().__init__(name, age, occupation)

    def think(self):
        print("The A`perform_task()` online.")

    def communicate(self):
        print("The AI is communicating digitally with its human.")

    def learn(self):
        print("The AI is learning and improving its capabilities.")
    
    def analize(self):
        print("The AI is analizing data and making predictions.")

class Robot(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        self.battery_level = 100
        super().__init__(name, age, occupation)

    def perform_task(self):
        print("The robot is performing a task with precision.")

robot = Robot("Robo", 10, "Factory Worker", 8.5)
my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
ai1 = AI("Gerardo", 19, "Virtual Assistant", 9.8)
print(robot.name)
print(robot.age)
print(robot.occupation)
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()
ai1.analize()
robot.perform_task()