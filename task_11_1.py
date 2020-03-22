from time import sleep


class AppsFromStore:
    def __init__(self, category='', size=0, user_rating=0, review=''):
        self.__category = category
        self.__size = size
        self.__user_rating = user_rating
        self.review = review

    def __str__(self):
        return f'Category: {self.__category}\n' \
               f'Size: {self.__size} Mb\n' \
               f'User rating: {self.__user_rating}\n' \
               f'Review: "{self.review}"'

    @property
    def category(self):
        return self.__category

    @category.setter
    def category_set(self, new_value):
        self.__category = new_value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size_set(self, new_value):
        self.__size = new_value

    @property
    def user_rating(self):
        return self.__category

    @user_rating.setter
    def user_rating_set(self, new_value):
        self.__category = new_value

    def write_review(self):
        self.review = input('Write review: ')

    def del_review(self):
        self.review = ''


class Worker:
    def __init__(self, name='', surname='', qualification=1):
        self.__name = name
        self.__surname = surname
        self.__qualification = qualification
        self.salary = 0
        self.tax = 0

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Surname: {self.__surname}\n' \
               f'Qualification: {self.__qualification}\n' \
               f'Salary: {self.salary}$\n' \
               f'Tax: {self.tax}$'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_set(self, new_value):
        self.__name = new_value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname_set(self, new_value):
        self.__surname = new_value

    @property
    def qualification(self):
        return self.__qualification

    @qualification.setter
    def user_rating_set(self, new_value):
        self.__qualification = new_value

    def calc_salary(self):
        self.salary = self.__qualification * 500
        return self.salary

    def calc_tax(self):
        if self.salary >= 1500:
            self.tax = self.salary * 0.15
            return self.tax
        else:
            self.tax = self.salary * 0.15
            return self.tax


class RepairElectronics:
    @property
    def cost(self):
        return self._cost

    def __init__(self, name='', problem='', condition=0):
        self.__name = name
        self.__problem = problem
        self.__condition = condition
        self.cost = 0

    def __str__(self):
        return f'Devise: {self.__name}\n' \
               f'Problem: {self.__problem}\n' \
               f'Condition: {self.__condition}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_set(self, new_value):
        self.__name = new_value

    @property
    def problem(self):
        return self.__problem

    @problem.setter
    def problem_set(self, new_value):
        self.__problem = new_value

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition_set(self, new_value):
        self.__condition = new_value

    def fix_cost(self):
        self.cost = (10 - self.condition) * 10
        return self.cost

    def fix(self):
        print('Repairing...')
        self.__condition = 10

    @cost.setter
    def cost(self, value):
        self._cost = value


class Weapon:
    def __init__(self, gun_type='', fire_rate=0.0, clip=0):
        self.__gun_type = gun_type
        self.__fire_rate = fire_rate
        self.__clip = clip

    def __str__(self):
        return f'Gun type: {self.__gun_type}\n' \
               f'Fire rate: {self.__fire_rate}\n' \
               f'Clip: {self.__clip}'

    @property
    def gun_type(self):
        return self.__gun_type

    @gun_type.setter
    def type_set(self, new_value):
        self.__gun_type = new_value

    @property
    def fire_rate(self):
        return self.__fire_rate

    @fire_rate.setter
    def problem_set(self, new_value):
        self.__fire_rate = new_value

    @property
    def clip(self):
        return self.__clip

    @clip.setter
    def clip_set(self, new_value):
        self.__clip = new_value

    def shot(self):
        print('Shooting...')
        for i in range(self.__clip):
            print('Piu...')
            sleep(self.__fire_rate)

    @staticmethod
    def reload():
        print('Reloading...')


class Pet:
    def __init__(self, name='', age=0, size=0.0):
        self.__name = name
        self.__age = age
        self.__size = size

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Age: {self.__age}\n' \
               f'Size: {self.__size}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_set(self, new_value):
        self.__name = new_value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age_set(self, new_value):
        self.__age = new_value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size_set(self, new_value):
        self.__size = new_value

    @staticmethod
    def walk():
        print('Walking...')
        sleep(1)
        print('Have been walking!')

    @staticmethod
    def eat():
        print('Eating...')
        sleep(1)
        print('Have been eating!')
