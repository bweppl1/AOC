# sample for visual
# 1-2 x: xpxc
# Answer: how many passwords meet the criteria


def main():
    with open("2data_set.csv", "r") as file:
        passwords = file.readlines()

        all_pws = []

        for password in passwords:
            all_pws.append(password)

    correct_passwords = 0

    for i in range(len(all_pws) - 1):
        # get password
        item = all_pws[i].split(":")
        password = item[1].strip()
        print(f"{password}")

        # get first index
        char_range = item[0].split("-")
        first_index = int(char_range[0]) - 1
        print(f"min: {min}")

        # get 2nd index
        max_dirty = char_range[1].split(" ")
        second_index = int(max_dirty[0]) - 1
        print(f"max: {max}")

        # get char
        char = max_dirty[1]
        print(f"char: {char}")

        # validation logic
        char_found_counter = 0

        if password[first_index] == char:
            char_found_counter += 1

        if password[second_index] == char:
            char_found_counter += 1

        if char_found_counter == 1:
            correct_passwords += 1

    print(f"correct passwords: {correct_passwords}")

    # i += 1  # remove after tsting complete


if __name__ == "__main__":
    main()
