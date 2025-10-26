amount = int(input("Enter the amount: "))
denom = int(input("Enter the denomination: "))
d = [100, 50, 20, 10, 5, 2, 1]

start_index = d.index(denom)
rem = amount

for i in d[start_index:]:
    notes = rem // i
    rem = rem % i

    match i:
        case 100:
            print(f"100 rupees note: {notes}")
        case 50:
            print(f"50 rupees note: {notes}")
        case 20:
            print(f"20 rupees note: {notes}")
        case 10:
            print(f"10 rupees note: {notes}")
        case 5:
            print(f"5 rupees note: {notes}")
        case 2:
            print(f"2 rupees note: {notes}")
        case 1:
            print(f"1 rupees note: {notes}")