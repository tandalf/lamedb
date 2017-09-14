class FileStudentLoader():
    def __init__(self, path):
        """
        Initializes a school information from the file path provided in the arguement

        Args:
            path: the file path on the filesystem where the file is exists
        """
        raise NotImplementedError("__init__ not implemented")

    def student_count(self):
        """
        Gets the amount of students in the file
        """
        raise NotImplementedError("student_count not implemented")

    def student_names(self):
        """
        Gets a list of firstname, and lastname entries that are present in the file.
        The list should be returned in the same order as it is in the file.

        Returns:
            list: a list of (firstname, lastname) tuples for every student in the file
        """
        raise NotImplementedError("student_names not implemented")

    def youngest_age(self):
        """
        Gets the age of the youngest student in the file.

        Returns:
            int: an integer the age of the youngest person in the students file
        """
        raise NotImplementedError("youngest_age not implemented")

    def average_age(self):
        """
        Gets the average age of the students in the students file.

        Returns:
            float: a floating point value of the average of students ages in the students file
        """
        raise NotImplementedError("average_age not implemented")
