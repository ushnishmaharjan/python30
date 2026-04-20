def test(a, b, c):
    return a


print(test(1, 2, 3))


def sum_data(a, b, c):
    return a + b + c


print(sum_data(1, 2, 3))
print(sum_data(100, 1123, 1213))

print("--------" * 10)


def add_list(data):
    add = 0
    for i in data:
        add = add + i

    return add


print(add_list([1, 2, 3, 4, 5, 6]))
print(add_list([100, 200, 300, 400, 500]))


print("--------" * 10)


def user_info(fname, lname):
    data = f"fname is {fname}  lname is {lname}"
    return data


print(user_info("sudan", "bhandari"))
print(user_info("bhandari", "sudan"))

print(user_info(lname="bhandari", fname="sudan"))

print("--------" * 10)


def count_vowels(word):

    if isinstance(word, str):
        vowel_count = 0
        word = word.lower()
        vowel = ["a", "e", "i", "o", "u"]

        for i in word.lower():
            if i in vowel:
                vowel_count += 1
        return vowel_count
    else:
        return f"error: {word} is not a string"


print(count_vowels("program"))
print(count_vowels(1))


def user_info(fname, lname="Sharma"):
    data = f"fname is {fname}  lname is {lname}"
    return data


print(user_info("sudan"))
print(user_info("hari", "khadka"))


def sum_number(*args):
    add = 0
    for i in args:
        add = add + i
    return add


print(sum_number(1, 2, 3, 4, 5))
print(sum_number(100, 200, 300, 400, 500))


print(sum_number(1, 1, 2, 3, 4, 2, 6, 1, 6, 7))


def test_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


test_kwargs(name="sudan", adress="nepal")

print("--------" * 10)


def schedule(*args, **kwargs):
    name = "The attendees requested to come are:  "
    details = f"the details of the schedule are: {kwargs}"
    return name, details


print(
    schedule(
        "hari",
        "ram",
        "shyam",
        day="sunday",
        time="10:00",
        place="sankhamul",
        phone=9801537672,
    )
)

print("--------" * 10)
