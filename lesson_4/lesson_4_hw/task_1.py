try:
    with open("emails.txt", encoding="UTF-8") as file_emails:
        with open("result.txt", "a", encoding="UTF-8") as f:
            for line in file_emails:
                if line.strip().endswith('@gmail.com'):
                    f.writelines(line.split()[-1] + '\n')
except Exception as error:
    print(error)
