import traceback


def merge_sort(A):
    sublist_size = 2
    while sublist_size < len(A):
        for index in range(0, len(A), sublist_size):
            left_sublist = A[index : index + (sublist_size // 2)]
            right_sublist = A[index + (sublist_size // 2) : index + sublist_size]
            left_index = 0
            right_index = 0
            temp_list = []
            while (
                left_index != len(left_sublist)
                and right_index != len(right_sublist)
                and len(temp_list) != sublist_size
            ):
                # Adds the left sublist value by default if values are equal
                if left_sublist[left_index] >= right_sublist[right_index]:
                    temp_list.append(left_sublist[left_index])
                    left_index += 1
                else:
                    temp_list.append(right_sublist[right_index])
                    right_index += 1
            if left_index == len(left_sublist):
                temp_list += right_sublist[right_index:]
            elif right_index == len(right_sublist):
                temp_list += left_sublist[left_index:]
            for temp_index, temp_value in enumerate(temp_list):
                A[index + temp_index] = temp_value
        sublist_size *= 2
    # Final Merge
    left_sublist = A[: sublist_size // 2]
    right_sublist = A[sublist_size // 2 :]
    left_index = 0
    right_index = 0
    temp_list = []
    while (
        left_index != len(left_sublist)
        and right_index != len(right_sublist)
        and len(temp_list) != sublist_size
    ):
        # Adds the left sublist value by default if values are equal
        if left_sublist[left_index] >= right_sublist[right_index]:
            temp_list.append(left_sublist[left_index])
            left_index += 1
        else:
            temp_list.append(right_sublist[right_index])
            right_index += 1
    if left_index == len(left_sublist):
        temp_list += right_sublist[right_index:]
    elif right_index == len(right_sublist):
        temp_list += left_sublist[left_index:]
    for temp_index, temp_value in enumerate(temp_list):
        A[temp_index] = temp_value
    return A


# Email class
# Each email has two instance variables:
#   self.sender is a string representing the name of the person
#     or organization that sent the email
#   self.subject is a stirng representing the subject line of
#     the Email
# You can create new methods, but don't change the existing ones.
class Email:
    def __init__(self, sender, subject):
        self.sender = sender
        self.subject = subject

    def __repr__(self):
        return "\n{:20}:{}".format(self.sender, self.subject)

    def __lt__(self, other):
        return len(self.sender) < len(other.sender)

    def __gt__(self, other):
        return len(self.sender) > len(other.sender)

    def __le__(self, other):
        return len(self.sender) <= len(other.sender)

    def __ge__(self, other):
        return len(self.sender) >= len(other.sender)

    def __eq__(self, other):
        return len(self.sender) == len(other.sender)

    def __ne__(self, other):
        return len(self.sender) != len(other.sender)


if __name__ == "__main__":
    # Setup test cases
    e1 = Email("Inigo Montoya", "You killed my father. Prepare to die.")
    e2 = Email("IRS", "THIS IS YOUR FINAL WARNING")
    e3 = Email("Your Grandson", "Need Money for College")
    e4 = Email("Prince of Nigeria", "Help transferring funds")
    e5 = Email("Jackpot Lottery", "YOU'RE WINNER!")
    e6 = Email("Super Antivirus Pro", "Virus Detected! Download Now!")
    e7 = Email("Anonymous", "Forward this to 20 friends and you will get $$$")
    e8 = Email("The Bank", "Please confirm your password")

    e9 = Email("Ted", "HAHAHAHAHAHAHAHAHAHA")
    e10 = Email("Tedd", "mine!")
    e11 = Email("Teddd", "be")
    e12 = Email("Tedddd", "will")
    e13 = Email("Teddddd", "Vengeance")
    e14 = Email("Tedddddd", "day.")
    e15 = Email("Teddddddd", "this")
    e16 = Email("Tedddddddd", "for")
    e17 = Email("Teddddddddd", "waited")
    e18 = Email("Tedddddddddd", "I")
    e19 = Email("Teddddddddddd", "have")
    e20 = Email("Tedddddddddddd", "Long")

    inbox1 = []
    inbox2 = [e13]
    inbox3 = [e2, e6]
    inbox4 = [e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20]
    inbox5 = [e20, e19, e18, e17, e16, e15, e14, e13, e12, e11, e10, e9]
    inbox6 = [e1, e2, e3, e4, e5, e6, e7, e8]

    tests = [inbox1, inbox2, inbox3, inbox4, inbox5, inbox6]

    correct = [
        [],
        [e13],
        [e6, e2],
        [e20, e19, e18, e17, e16, e15, e14, e13, e12, e11, e10, e9],
        [e20, e19, e18, e17, e16, e15, e14, e13, e12, e11, e10, e9],
        [e6, e4, e5, e1, e3, e7, e8, e2],
    ]

    # Run test cases, check whether sorted list correct
    count = 0

    try:

        for i in range(len(tests)):
            print("TEST #" + str(i + 1))
            print("Running: merge_sort(", tests[i], ")\n")
            merge_sort(tests[i])
            print("Expected:", correct[i], "\n\nGot:", tests[i])
            assert correct[i] == tests[i], "List sorted incorrectly"
            count = count + 1
            print("\n---------------------------------------\n")

    except AssertionError as e:
        print("\nFAIL: ", e)
    except Exception:
        print("\nFAIL: ", traceback.format_exc())

    print(count, "out of", len(tests), "tests passed.")
