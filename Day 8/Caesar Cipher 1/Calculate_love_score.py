def calculate_love_score(name1, name2):
    both_names = (name1+name2).lower()
    print(both_names)
    true_letters = "TRUE".lower()
    love_letters = "LOVE".lower()
    true_count = 0
    love_count = 0
    count = 0
    for char in true_letters:
        count = 0
        for ch in both_names:
            if ch == char:
                count += 1
        print(f"{char} occurs {count} times.")
        true_count += count
    print(true_count)

    for char in love_letters:
        count = 0
        for ch in both_names:
            if ch == char:
                count += 1
        print(f"{char} occurs {count} times.")
        love_count += count
    print(love_count)

    print(f"{true_count}{love_count}")

calculate_love_score("Angela Yu", "Jack Bauer")