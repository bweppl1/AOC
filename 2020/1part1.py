# Find the 2 values that sum to 2020
# The factor of those 2 values is the answer


def main():
    with open("1data_set.csv", "r") as file:
        amounts = file.readlines()

        target = 2020
        all_values = []

        for amount in amounts:
            all_values.append(int(amount))

        all_values.sort()
        l = 0
        r = len(all_values) - 2

        # FOR TESTING
        # print(f"first value: {all_values[l]}")
        # print(f"last value: {all_values[r]}")

        while l < r:
            current = all_values[l] + all_values[r]

            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else:
                value_one = all_values[l]
                value_two = all_values[r]
                print(
                    f"value1: {value_one} index1: {l}, value2: {value_two} index2: {r}"
                )
                answer = value_one * value_two
                break

        print(f"ANSWER FOUND: {answer}")


if __name__ == "__main__":
    main()
