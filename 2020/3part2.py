#
# Right 1, down 1.  85
# Right 3, down 1.  176
# Right 5, down 1.  96
# Right 7, down 1.  87
# Right 1, down 2.  47
#
def main():

    all_rows = []

    with open("3data_set", "r") as file:
        rows = file.readlines()

        for row in rows:
            all_rows.append(row.strip())

    trees_hit = 0
    i = 0
    skip_flag = 0
    print(f"Row Count: {len(all_rows)}")

    for row in all_rows:
        if skip_flag == 0:
            if i > len(row) - 1:
                i = i - (len(row))
            if row[i] == "#":
                trees_hit += 1
            i += 1
            skip_flag = 1
        else:
            skip_flag = 0

    # while i < len(mega_row):
    #     if mega_row[i] == "#":
    #         trees_hit += 1
    #     i += row_length + 2

    print(f"Trees hit: {trees_hit}")

    factor_result = 85 * 176 * 96 * 87 * 47
    print(f"FACTOR: {factor_result}")


if __name__ == "__main__":
    main()
