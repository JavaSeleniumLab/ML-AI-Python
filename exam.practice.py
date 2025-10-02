class MyClass:
    def run(self):
        my_list = [1, 'a', 99, "Alina"]
        my_list.append('appended')
        print(my_list)

        my_list.pop()
        print(my_list)

        tuple_one = (5, 6, 7, 8)
        print(tuple_one)

        dict_one = {"name": "Alina", "age": 25}
        dict_one.get("hobby")
        print(dict_one.keys())
        print(dict_one)
        print("================0000========0000========")
        print(dict_one.items())
        print(dict_one.get("hobby", "default value"))
        print("================1111=======1111=========")
        # Example 1: key does not exist, returns default
        example_dict = {'a': 1, 'b': 2}
        result1 = example_dict.get('c', 'not found')
        print(result1)  # Output: not found
        # Example 2: key exists, returns value
        result2 = example_dict.get('a', 'not found')
        print(result2)  # Output: 1
        # Example 3: key does not exist, no default provided (returns None)
        result3 = example_dict.get('d')
        print(result3)  # Output: None
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = list1 + list2
        print(list3)
        mytuple = (1, 2, 3, 4, 5)
        print(mytuple[2])
        my_set = {1, 2, 3, 4, 5}
        print(my_set)
        my_set.clear()
        print(my_set)
        print({1,2,3} | {3,4,5})
        print(len([1, 3, 'a']))

# To run all code in the class:
if __name__ == "__main__":
    MyClass().run()
