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

        # get minimum
        char_range = item[0].split("-")
        min = int(char_range[0])
        print(f"min: {min}")

        # get maximum
        max_dirty = char_range[1].split(" ")
        max = int(max_dirty[0])
        print(f"max: {max}")

        # get char
        char = max_dirty[1]
        print(f"char: {char}")

        char_count = 0
        for c in password:
            if c == char:
                char_count += 1

        if char_count > max or char_count < min:
            pass
        else:
            correct_passwords += 1

        print(f"correct passwords: {correct_passwords}")

        # i += 1  # remove after tsting complete


if __name__ == "__main__":
    main()
