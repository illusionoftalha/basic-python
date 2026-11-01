import contextlib
import io
import unittest

from lessons.beginner.conditions import grade
from lessons.beginner.functions import average
from lessons.beginner.input_output import greeting
from lessons.intermediate.decorators import add
from lessons.intermediate.exceptions import positive_integer
from lessons.intermediate.generators import countdown
from lessons.intermediate.objects import Book


class LearningTests(unittest.TestCase):
    def test_grade_boundaries(self):
        for score, expected in [(0, "F"), (49, "F"), (50, "D"), (60, "C"),
                                (70, "B"), (79, "B"), (80, "A"), (100, "A")]:
            with self.subTest(score=score):
                self.assertEqual(grade(score), expected)

    def test_grade_rejects_invalid_input(self):
        for score in [-1, 101, True, 80.5, "80"]:
            with self.subTest(score=score), self.assertRaises(ValueError):
                grade(score)

    def test_average_handles_negative_values_and_empty_input(self):
        self.assertEqual(average([-10, 0, 10]), 0)
        self.assertEqual(average([4]), 4)
        with self.assertRaises(ValueError):
            average([])

    def test_greeting_trims_whitespace_and_rejects_blank_name(self):
        self.assertEqual(greeting("  Talha "), "Hello, Talha!")
        with self.assertRaises(ValueError):
            greeting("   ")

    def test_positive_integer(self):
        self.assertEqual(positive_integer("12"), 12)
        for text in ["0", "-1", "abc", "1.5"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                positive_integer(text)

    def test_generator_is_lazy_and_exhausted_after_iteration(self):
        counter = countdown(3)
        self.assertEqual(next(counter), 3)
        self.assertEqual(list(counter), [2, 1])
        self.assertEqual(list(counter), [])
        self.assertEqual(list(countdown(0)), [])
        with self.assertRaises(ValueError):
            list(countdown(-1))

    def test_book_cannot_be_borrowed_twice(self):
        book = Book("Python")
        book.borrow()
        with self.assertRaises(ValueError):
            book.borrow()
        book.return_book()
        book.borrow()
        self.assertTrue(book.borrowed)

    def test_decorator_preserves_result_and_function_metadata(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(add(2, right=3), 5)
        self.assertEqual(add.__name__, "add")
        self.assertIn("Add two numbers", add.__doc__)
        self.assertIn("Calling add", output.getvalue())
