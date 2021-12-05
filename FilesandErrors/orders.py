
def open_and_print_file(file):
    try:
        with open(file, "r") as opened_file:
            file_line_list = opened_file.readlines()

            for line in file_line_list:
                print(line.replace("\n", ""))


    except FileNotFoundError as errmsg:
        print('There is no file, panic!',errmsg)

    finally:
        print('Execution Complete')

# open_and_print_file("order.txt")


def write_to_file(file, order_item):
    try:
        with open(file, "w") as file_to_write:
            file_to_write.write(order_item+'\n')
    except FileNotFoundError:
        print("Fil doesn't exist")

write_to_file("order.txt", "Onion Rings")
open_and_print_file("order.txt")
