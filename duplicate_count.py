def duplicate_count(text):
    how_much = 0
    checklist = []
    for c in text:
        if text.count(c) > 1:
            if not c in checklist:
                how_much = how_much + 1
            checklist.append(c)
            print (checklist)

    print (how_much)


duplicate_count("abcde")
duplicate_count("abcdea")
duplicate_count("indivisibility")
