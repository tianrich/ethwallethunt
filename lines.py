with open("generated.txt", "r") as file:
    lines = file.readlines()

with open("generated.txt", "w") as file:
    lines = [line for line in lines if line.strip()]
    file.writelines(lines)
