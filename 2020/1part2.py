# Find the 3 values that sum to 2020
# The factor of those 3 values is the answer


def main():
    with open("1data_set.csv", "r") as file:
        amounts = file.readlines()

        target = 2020
        all_values = []

        for amount in amounts:
            all_values.append(int(amount))

    all_values.sort()

    # for debug/test
    counter = 0

    for i in range(len(all_values) - 2):
        l = i + 1
        r = len(all_values) - 1

        while l < r:
            three_sum = all_values[i] + all_values[l] + all_values[r]

            if three_sum > target:
                r -= 1
                counter += 1
            elif three_sum < target:
                l += 1
                counter += 1
            elif three_sum == target:
                v1 = all_values[i]
                v2 = all_values[l]
                v3 = all_values[r]

                answer = v1 * v2 * v3

                # FOR TESTING
                # print(f"first value: {all_values[l]}")
                # print(f"last value: {all_values[r]}")

                print(f"ANSWER FOUND: {answer}")
                break
        counter += 1

    print(f"Program ended. No answer found after {counter} attemps.")


if __name__ == "__main__":
    main()
