import sys

try:
    with open("emailqs.txt", encoding="UTF-8") as file_emails:
        with open("result.txt", "a", encoding="UTF-8") as f:
            for line in file_emails:
                if line.strip().endswith('@gmail.com'):
                    print(line.split()[-1])
                    f.writelines(line.split()[-1] + '\n')
except Exception:
    print(sys.exc_info()[1])
