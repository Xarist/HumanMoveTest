import unittest
from main import Student


class StudentTest(unittest.TestCase):

    def test_walk(self):
        student = Student('Walker')
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, f"Дистанции {student.__str__()} не равны: {student.distance} != 500")

    def test_run(self):
        student = Student('Runner')
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, f"Дистанции {student.__str__()} не равны: {student.distance} != 1000")

    def test_run_vs_walk(self):
        walker = Student('Walker')
        runner = Student('Runner')
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertGreater(runner.distance, walker.distance, f"{runner.__str__()} должен преодоленть дистанцию больше, чем {walker.__str__()}")
        # self.assertEqual(runner.distance, walker.distance, f"{runner.__str__()} должен преодоленть дистанцию больше, чем {walker.__str__()}")
        # self.assertLess(runner.distance, walker.distance, f"{runner.__str__()} должен преодоленть дистанцию больше, чем {walker.__str__()}")


if __name__ == '__main__':
    unittest.main()

