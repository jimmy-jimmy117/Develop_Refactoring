import unittest
from exercise1 import check_and_repeat  # 実際のモジュール名に置き換えてください


class TestCheckAndRepeat(unittest.TestCase):

    # 正常系のテスト
    def test_valid_input(self):
        # 正常なケース: "Hello"を横に3回、縦に2回繰り返す
        result = check_and_repeat("Hello", 3, 2)
        expected = "HelloHelloHello\nHelloHelloHello"
        self.assertEqual(result, expected)

    # 異常系のテスト: 文字列の長さが5未満の場合
    def test_invalid_length_too_short(self):
        with self.assertRaises(ValueError):
            check_and_repeat("Hi", 3, 2)  # 長さが2なのでエラー

    # 異常系のテスト: 文字列の長さが10を超える場合
    def test_invalid_length_too_long(self):
        with self.assertRaises(ValueError):
            check_and_repeat("ThisIsTooLong", 3, 2)  # 長さが14なのでエラー

    # 異常系のテスト: アルファベット以外の文字が含まれている場合
    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            check_and_repeat("Hello123", 3, 2)  # 数字が含まれているのでエラー

    # 異常系のテスト: 空文字列の場合
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            check_and_repeat("", 3, 2)  # 空文字列なのでエラー

    # 異常系のテスト: 数値が負の場合
    def test_negative_num1(self):
        with self.assertRaises(ValueError):
            check_and_repeat("Hello", -1, 2)  # num1が負数なのでエラー

    def test_negative_num2(self):
        with self.assertRaises(ValueError):
            check_and_repeat("Hello", 3, -2)  # num2が負数なのでエラー


if __name__ == "__main__":
    unittest.main()
