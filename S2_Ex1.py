class School:
    def __init__(self, ages, heights, weights):
        self.students_ages = ages
        self.students_height = heights
        self.students_weight = weights

    def get_age_ave(self):
        return float(sum(self.students_ages) / len(self.students_ages))

    def get_height_ave(self):
        return float(sum(self.students_height) / len(self.students_height))

    def get_weight_ave(self):
        return float(sum(self.students_weight) / len(self.students_weight))

    def __ge__(self, other):
        height1 = self.get_height_ave()
        weight1 = self.get_weight_ave()
        height2 = other.get_height_ave()
        weight2 = other.get_weight_ave()
        if height1 > height2:
            return 'A'
        elif height1 < height2:
            return 'B'
        elif height1 == height2 and weight1 < weight2:
            return 'A'
        elif height1 == height2 and weight1 > weight2:
            return 'B'
        elif height1 == height2 and weight1 == weight2:
            return 'Same'


number_of_students_A = int(input())
age_students_A = str(input())
height_students_A = str(input())
weight_students_A = str(input())

age_list_A = [int(i) for i in age_students_A.split()]
height_list_A = [int(i) for i in height_students_A.split()]
weight_list_A = [int(i) for i in weight_students_A.split()]

number_of_students_B = int(input())
age_students_B = str(input())
height_students_B = str(input())
weight_students_B = str(input())

age_list_B = [int(i) for i in age_students_B.split()]
height_list_B = [int(i) for i in height_students_B.split()]
weight_list_B = [int(i) for i in weight_students_B.split()]

school_A = School(age_list_A, height_list_A, weight_list_A)
print(school_A.get_age_ave())
print(school_A.get_height_ave())
print(school_A.get_weight_ave())

school_B = School(age_list_B, height_list_B, weight_list_B)
print(school_B.get_age_ave())
print(school_B.get_height_ave())
print(school_B.get_weight_ave())

print(school_A >= school_B)
