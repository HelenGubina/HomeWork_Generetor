my_dict = {
  "name": "Helen",
  "surname": "Gubina",
  "sex": "female"
}

my_dict_iter = my_dict.keys().__iter__()
while True:
    try:
        print(next(my_dict_iter))
    except StopIteration:
        break

