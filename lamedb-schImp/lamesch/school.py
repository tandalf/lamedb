class FileStudentLoader(object):

    def __init__(self, path):
        fr = open(path, "r")
        self.Firstnames = []
        self.Lastname = []
        self.ages = []
        for i in fr.readlines():
            Firstname, Lastname, Age, remark, rank = i.split(",")
            self.Firstnames.append(Firstname)
            self.Lastname.append(Lastname)
            self.ages.append(Age)

        #print(self.Firstnames, self.Lastname, self.ages)
        fr.close()

    def student_count(self):
        # total_count = []
        # count = self.ages[1:]
        # for i in count:
        #     total_count.append(i)
        number = len(self.Lastname[1:])
        #print(number)
        return number

    def student_names(self):
        last_name = []
        names = []
        firstname = self.Firstnames
        lastname = self.Lastname
        for i in lastname:
            last = i.strip(" ")
            last_name.append(last)
        for i in range(0, len(last_name)):
            name = firstname[i], last_name[i]
            names.append(name)
        names = names[1:]
        # for key, value in firstname:
        #     name = firstname[0]
        #print(names)
        return names

    def youngest_age(self):
        self.young = []
        youngest = self.ages[1:]
        for i in youngest:
            self.young.append(int(i))
        minimum = min(self.young)
        #print(minimum)
        return int(minimum)

    def average_age(self):
        avg_age = []
        average = self.ages[1:]
        for i in average:
            avg_age.append(int(i))
        # for i in self.young:
        #     average.append(i)
        avg = sum(avg_age) / float(len(avg_age))
        #print(avg, "\n")
        return avg


studentfile = FileStudentLoader(r"C:\Users\Tayo\PycharmProjects\untitled\lamedb-schImp\db\file_student_test_db.txt")
studentfile.student_count()
studentfile.student_names()
studentfile.youngest_age()
studentfile.average_age()
