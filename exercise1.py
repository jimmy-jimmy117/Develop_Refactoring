import re


def check_and_repeat(input_str: str, num1: int, num2: int):
    """_summary_
    文字列の長さチェック
    文字列が5文字以上、10文字以下であることを確認

    Args:
        input_str (str): Pythonの文字列は、str型として扱われます。
        文字列は、シングルクォート (') やダブルクォート (") で囲むことで表現します。
        num1 (int): Pythonのint型は整数を表現します。整数には、小数点は含まれません。
        num2 (int): Pythonのint型は整数を表現します。整数には、小数点は含まれません。

    Raises:
        ValueError: アルファベット以外の文字が含まれている場合、ValueErrorを発生させる
        ValueError: アルファベット以外の文字が含まれている場合、ValueErrorを発生させる

    Returns:
        _type_: 最後の余分な改行を削除して返す
    """
    # 1. 文字列の長さチェック
    if not (5 <= len(input_str) <= 10):
        raise ValueError("エラー: 文字列は5文字以上10文字以下である必要があります。")

    # 2. アルファベット以外の文字が含まれていないかチェック
    if not re.match("^[a-zA-Z]+$", input_str):
        raise ValueError("エラー: 文字列にはアルファベット以外の文字が含まれています。")

    # 3. 文字列を横に最初の数値分繰り返し、縦に次の数値分繰り返す
    result = (input_str * num1 + "\n") * num2
    return result.strip()  # 最後の改行を削除して返す
