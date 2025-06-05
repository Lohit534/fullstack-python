with open("students.txt", "w") as f:
    f.writelines(["Alice\n", "Bob\n", "Charlie\n"])

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())
