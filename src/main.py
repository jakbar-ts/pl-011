def file_sum(file_path):
    sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            numbers = [int(n) for n in line.split("; ")]
            for n in numbers:
                sum += n
    return sum