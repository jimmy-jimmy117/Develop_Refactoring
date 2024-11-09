import random


def print_random():
    # 0〜1億の範囲でランダムな数を100万個生成
    large_list = [random.randint(0, 100000000) for _ in range(1000000)]

    # 0〜1億の範囲でランダムな数を100個生成
    target_list = [random.randint(0, 100000000) for _ in range(100)]

    # リストの部分一致を高速にチェックするために、setを使う
    large_set = set(large_list)  # large_listをセットに変換して検索を高速化

    # target_listの全要素がlarge_setに含まれているかをチェック
    if all(item in large_set for item in target_list):
        print(f"Found the target list: {target_list}")


if __name__ == "__main__":
    print_random()
