class Student:
    # STATIC STATE---->VAR=VALUE--->STORED IN CLASS MEMORY
    sub = "python"
    class_timing = "5:30pm - 7:30pm"
    room_num = 3
    no_of_class = 52
    no_of_student = 0
    student_db = {}

    def __init__(self, name, mobile, age, yop, attendance):
        self.std_name = name
        self.std_mobile = self.validate_mobile(mobile)
        self.std_age = self.validate_age(age)
        self.std_yop = yop
        self.std_attendance = attendance
        self.std_id = "py" + str(self.gen_id())
        self.student_db[self.std_id] = self

    @classmethod
    def gen_id(cls):
        cls.no_of_student += 1
        return cls.no_of_student

    @classmethod
    def all_std_data(cls):
        print("="*85)
        print(f"{'STD_ID':<10} {'NAME':<15} {'MOBILE':<12} {'AGE':<5} {'YOP':<6} {'ATTENDANCE':<10}")
        print("="*85)
        for obj in cls.student_db.values():
            print(f"{obj.std_id:<10} {obj.std_name:<15} {obj.std_mobile:<12} {obj.std_age:<5} {obj.std_yop:<6} {obj.std_attendance:<10}")
        print("="*85)

    def modify_std_data(self):
        while True:
            print("-" * 30)
            print("SELECT 1 FOR CHANGING THE NAME\nSELECT 2 FOR CHANGING THE AGE\nSELECT 3 FOR CHANGING THE YOP\nSELECT 4 FOR CHANGING THE MOBILE\nSELECT 5 TO EXIT\n")
            select = int(input("select a option:"))
            match select:
                case 1:
                    new_name = input("enter the new name:")
                    self.std_name = new_name
                    print("name changed successfully")
                case 2:
                    new_age = input("enter the new age:")
                    self.std_age = self.validate_age(int(new_age))
                    print("age changed successfully")
                case 3:
                    new_yop = input("enter the new yop:")
                    self.std_yop = new_yop
                    print("yop changed successfully")
                case 4:
                    self.modify_mobile()
                case 5:
                    print("thanks for modifying")
                    break
                case _:
                    print("select options from 1-5")

    @staticmethod
    def validate_mobile(user_number):
        st_num = str(user_number)
        if len(st_num) == 10 and st_num[0] in "6789":
            return user_number
        else:
            raise Exception("invalid number")

    @staticmethod
    def validate_age(user_age):
        if 18 <= user_age <= 60:
            return user_age
        else:
            raise Exception("invalid age. Age should be 18-60")

    # INSTANCE METHOD
    def get_student_data(self):
        print(F"----------------{self.std_name.upper()} DATA---------------\n")
        print(f"STUDENT ID :{self.std_id}\nSTUDENT NAME :{self.std_name}\nSTUDENT MOBILE: {self.std_mobile}\n"
              f"STUDENT AGE : {self.std_age}\nSTUDENT YOP:{self.std_yop}\n"
              f"STUDENT ATTENDANCE : {self.std_attendance}\n")

    @classmethod
    def python_class_details(cls):
        print(f"{'*' * 30}\nSUB : {cls.sub}\nTIMING:{cls.class_timing}\nNO_OF_CLASS : {cls.no_of_class}\n"
              f"NO_OF_STD : {cls.no_of_student}\nROOM:{cls.room_num}\n{'*' * 30}")

    def student_name_and_sub(self):
        print(f"student name:{self.std_name}\nsub:{self.sub}\ntiming:{self.class_timing}\n")

    @classmethod
    def modify_timing(cls):
        cls.class_timing = "5:00pm-7:00pm"
        print("timings changed successfully")

    def modify_mobile(self):
        new_mobile = int(input("enter the new mobile number:"))
        confirm_mobile = int(input("confirm the mobile number:"))
        if new_mobile == confirm_mobile:
            self.std_mobile = self.validate_mobile(new_mobile)
            print("mobile num updated successfully\n")
        else:
            print("new mobile and confirm mobile are not matching")

    @classmethod
    def delete_student(cls):
        std_id = input("Enter Student ID to delete: ")
        if std_id in cls.student_db:
            del cls.student_db[std_id]
            cls.no_of_student -= 1
            print("Student deleted successfully")
        else:
            print("Student ID not found")

    @classmethod
    def add_student_data(cls):
        try:
            name = input("enter your name:").capitalize()
            mobile = int(input("enter your 10 digit mobile number:"))
            age = int(input("enter your age:"))
            yop = int(input("enter your yop:"))
            attendance = 0
            obj = cls(name, mobile, age, yop, attendance)
            print(f"student added successfully with id:{obj.std_id}")
        except Exception as e_msg:
            print(f"ERROR--> {e_msg}")

# ========== DEMO DATA START LO NE CREATE CHESTHUNAM ==========
std1 = Student("riyaz", 9552476210, 20, 2026, 30)
std2 = Student("manoj", 8647521835, 22, 2026, 48)

print("="*50)
print("WELCOME TO QSP - DEMO DATA")
print("="*50)

# PROGRAM START AYINA VENTANE ICHEPTUNAM
std1.get_student_data() # INSTANCE METHOD CALL
std2.get_student_data()

print("="*50)
print("NOW YOU CAN USE MENU")
print("="*50)
# ========== DEMO DATA END ==========

print("welcome to qsp menu")
while True:
    print("\n" + "=" * 40)
    print("SELECT 1 TO ADD STUDENT :\n"
          "SELECT 2 TO GET ALL THE STUDENT DATA\n"
          "SELECT 3 TO VIEW ONE STUDENT DATA\n"
          "SELECT 4 TO MODIFY STUDENT\n"
          "SELECT 5 TO DELETE STUDENT\n"
          "SELECT 8 TO EXIT:\n")

    try:
        select = int(input("select a option:"))

        match select:
            case 1:
                Student.add_student_data()
            case 2:
                Student.all_std_data()
            case 3:
                std_id = input("Enter Student ID to view: ")
                if std_id in Student.student_db:
                    Student.student_db[std_id].get_student_data()
                else:
                    print("Student ID not found")
            case 4:
                std_id = input("Enter Student ID to modify: ")
                if std_id in Student.student_db:
                    Student.student_db[std_id].modify_std_data()
                else:
                    print("Student ID not found")
            case 5:
                Student.delete_student()
            case 8:
                print("Thank you bye")
                break
            case _:
                print("Select options from 1-5 or 8")

    except Exception:
        print("ENTER THE DIGITS\n")
        continue