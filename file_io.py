with open('salary.txt', 'r') as rf:
    with open('output.txt', 'w') as wf:
        for lines in rf.readlines():
            name,salary = lines.split(',')
            wf.write(f"Monthly salary of {name} is {salary}")
        