from random import randint
from typing import List


class CodeKataPython2:

    def __init__(self):
        pass

    def random_from_list(self, nums):
        i = randint(0, len(nums) - 1)
        return nums[i]


class CodeKataPython3:

    def __init__(self):
        pass

    def random_from_list(self, nums: List[int]) -> int:
        i: int = randint(0, len(nums) - 1)
        return nums[i]


def global_function_python2():
    return 'my_test'


def global_function_python3() -> str:
    return 'my_test'
