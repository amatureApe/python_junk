import string
import time


def slowly_print_hello_world():
    target = "Hello World!"
    characters = (
        string.ascii_lowercase + string.ascii_uppercase + " " + "!"
    )  # Include uppercase letters and space
    current_string = ""
    target_index = 0

    while target_index < len(target):
        for char in characters:
            # Build the string to test - add the current character
            test_string = current_string + char

            # Print the current test string
            print(test_string)
            time.sleep(0.1)  # Slow down the printing for effect

            # Check if the test string matches the target string up to the current length
            if target.startswith(test_string):
                current_string = test_string
                if char == target[target_index]:
                    target_index += 1
                    break


slowly_print_hello_world()
