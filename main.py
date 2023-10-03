import sys


def hello_func(args):
    return "How can I help you?"


phonebook = {}


def input_error(func):
    def inner(args):
        try:
            func(args)
        except ValueError:
            print("Enter user name")
        except KeyError:
            print("Enter correct user name")
        except IndexError:
            print("IndexError: list index out of range")
        #return print(args)
    return inner


@input_error
def add_change_func(args):
    phonebook.update({args[1]: args[2]})


@input_error
def phone_func(args):
    print(phonebook[args[1]])


@input_error
def show_all_func(args):
    if args[0] + args[1] == "showall":
        print(phonebook)
    else:
        print("Incorrect command")


OPERATIONS = {
        'hello': hello_func,
        'add': add_change_func,
        'change': add_change_func,
        'phone': phone_func,
        'show': show_all_func,
    }


def get_handler(args):
    return OPERATIONS[args]


def main():
    cmd_exit = ["good bye", "close", "exit"]
    command = ""
    while True:
        command = input("Enter command: ")
        if command in cmd_exit:
            break
        args = command.split()
        get_handler(str(args[0]))(args)
    print("Good bay")


if __name__ == '__main__':
    main()
