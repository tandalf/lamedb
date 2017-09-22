import os
from unittest import TestCase

from lamesch.school import FileStudentLoader

class TestFileStudentLoader(TestCase):
    def setUp(self):
        self.path = os.path.join(__file__, '../../db/file_student_test_db.txt')

    def test_student_count(self):
        loader = FileStudentLoader(self.path)
        self.assertEqual(7, loader.student_count())

    def test_student_names(self):
        loader = FileStudentLoader(self.path)
        expected_names = [
            ('Tuwase', 'Ty'),
            ('Caleb', 'Ortserga'),
            ('Emma', 'Emma'),
            ('Mark', 'Zue'),
            ('Tim', 'Tim'),
            ('Bante', 'Bonk'),
            ('Oduduwa', 'Tuwase'),
        ]
        names = loader.student_names()
        self.assertListEqual(expected_names, names)
        #self.assertEqual(len(expected_names), len(names))

        #for expected_name in expected_names:
        #    self.assert
    def test_youngest_age(self):
        loader = FileStudentLoader(self.path)
        self.assertEqual(9, loader.youngest_age())

    def test_average_age(self):
        loader = FileStudentLoader(self.path)
        self.assertEqual(12.142857142857142, loader.average_age())

if __name__ =='__main__':
    TestCase.run()
