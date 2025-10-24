class Employee:
    def work(self):
        print("Employee works.")
class Manager(Employee):
    def manage(self):
        print("Manager manages the team .")
class SeniorManager(Manager):
    def lead(self):
        print("Senior Manager lead departments.")
sm=SeniorManager()
sm.work()
sm.manage()
sm.lead()