# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint


def get_dict_list() -> list[dict]:
    num_dict = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]
    return num_dict


pprint(get_dict_list())

