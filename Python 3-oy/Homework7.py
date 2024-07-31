class Student:
    def __init__(self, full_name, age, birthday, gender):
        """
        Initializes a Student object with basic attributes.

        Args:
        full_name (str): The full name of the student.
        age (int): The age of the student.
        birthday (str): The birthday of the student (format: "YYYY-MM-DD").
        gender (str): The gender of the student ("Male" or "Female").
        """
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = []

    def __str__(self):
        """
        Returns a string representation of the Student object.

        Returns:
        str: String representation of the Student object.
        """
        return f"Student({self.full_name}, {self.age}, {self.birthday}, {self.gender}, Courses: {len(self.courses)})"

    def __repr__(self):
        """
        Returns a detailed string representation of the Student object.

        Returns:
        str: Detailed string representation of the Student object.
        """
        return self.__str__()

    def __len__(self):
        """
        Returns the number of courses the student is enrolled in.

        Returns:
        int: Number of courses the student is enrolled in.
        """
        return len(self.courses)

    def __add__(self, other):
        """
        Adds another Student object to the courses list of the current student.

        Args:
        other (Student): Another Student object to be added to courses list.

        Returns:
        Student: Updated Student object after adding another student to courses list.
        """
        if isinstance(other, Student):
            self.courses.append(other)
        return self

    def __sub__(self, other):
        """
        Removes another Student object from the courses list of the current student.

        Args:
        other (Student): Another Student object to be removed from courses list.

        Returns:
        Student: Updated Student object after removing another student from courses list.
        """
        if isinstance(other, Student) and other in self.courses:
            self.courses.remove(other)
        return self

    def __mul__(self, other):
        """
        Duplicates the courses list of the current student a specified number of times.

        Args:
        other (int): Number of times to duplicate the courses list.

        Returns:
        Student: Updated Student object with duplicated courses list.
        """
        if isinstance(other, int):
            self.courses *= other
        return self

    def __truediv__(self, other):
        """
        Reduces the courses list of the current student by dividing its length.

        Args:
        other (int): Number by which to divide the length of the courses list.

        Returns:
        Student: Updated Student object with reduced courses list.
        """
        if isinstance(other, int) and other != 0:
            self.courses = self.courses[:len(self.courses) // other]
        return self

    def __iadd__(self, other):
        """
        Implements the += operation for adding another Student object.

        Args:
        other (Student): Another Student object to be added to courses list.

        Returns:
        Student: Updated Student object after adding another student to courses list.
        """
        return self.__add__(other)

    def __isub__(self, other):
        """
        Implements the -= operation for removing another Student object.

        Args:
        other (Student): Another Student object to be removed from courses list.

        Returns:
        Student: Updated Student object after removing another student from courses list.
        """
        return self.__sub__(other)

    def __imul__(self, other):
        """
        Implements the *= operation for duplicating the courses list.

        Args:
        other (int): Number of times to duplicate the courses list.

        Returns:
        Student: Updated Student object with duplicated courses list.
        """
        return self.__mul__(other)

    def __itruediv__(self, other):
        """
        Implements the /= operation for reducing the courses list.

        Args:
        other (int): Number by which to divide the length of the courses list.

        Returns:
        Student: Updated Student object with reduced courses list.
        """
        return self.__truediv__(other)

# Example usage:
if __name__ == "__main__":
    student1 = Student("John Doe", 20, "2003-01-01", "Male")
    student2 = Student("Jane Smith", 22, "2001-05-15", "Female")

    print(student1)  # Student(John Doe, 20, 2003-01-01, Male, Courses: 0)
    student1 += student2
    print(student1)  # Student(John Doe, 20, 2003-01-01, Male, Courses: 1)
    print(len(student1))  # 1
    student1 *= 2
    print(len(student1))  # 2
    student1 /= 2
    print(len(student1))  # 1
    student1 -= student2
    print(student1)  # Student(John Doe, 20, 2003-01-01, Male, Courses: 0)