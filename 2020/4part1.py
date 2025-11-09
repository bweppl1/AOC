# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# incorrect answers: 259


def main():
    valid_passports = 0
    passports = []
    passport = []
    possible_items = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    with open("4data_set", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.strip() == "":
                passport = "".join(passport)
                passports.append(passport)
                passport = []
            else:
                passport.append(line)

    def print_invalid(pp):
        print(f"**INVALID** {pp}")

    l = 0
    r = 3

    for passport in passports:
        valid_item_count = 0
        if passport[r] == ":":
            l = r - 3
            passport_item = passport[l:r]
            # byr
            if passport_item == "byr" or passport_item == "iyr":
                l = r + 1
                r = r + 4
                byr = passport[l:r]
                if int(byr) <= 2020:
                    valid_item_count += 1
                else:
                    print_invalid(passport)
                    r += 1 
            # iyr 
            #HANDELED IN byr

            # eyr 
            if passport_item == "eyr":
                l = r + 1
                r = r + 4
                eyr = passport[l:r]
                if eyr > 2020:
                    valid_item_count += 1
                else:
                    print_invalid(passport)
                    r += 1

            # hgt 
            if passport_item == "hgt":
                l = r + 1
                r = l + 2
                if passport[r] == "c" or passport[r] == "i":
                    hgt == 
            # hcl 
            # ecl 
            # pid 
            # cid

if __name__ == "__main__":
    main()
