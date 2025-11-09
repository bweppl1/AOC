def main():

    all_rows = []

    with open("3data_set", "r") as file:
        rows = file.readlines()

        for row in rows:
            all_rows.append(row.strip())

    trees_hit = 0
    i = 0
    print(f"Row Count: {len(all_rows)}")

    for row in all_rows:
        if i > len(row) - 1:
            i = i - (len(row))
        if row[i] == "#":
            trees_hit += 1
        i += 3

    # while i < len(mega_row):
    #     if mega_row[i] == "#":
    #         trees_hit += 1
    #     i += row_length + 2

    print(f"Trees hit: {trees_hit}")


if __name__ == "__main__":
    main()
