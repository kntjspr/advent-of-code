import re
from tkinter import filedialog


if __name__ == '__main__':
    calibration_sum = 0  
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    with open(file, "r") as file:
        for line in file:
            line = line.strip() 
            line = re.sub(r"\D", "", line)
            if line:
                first_digit = int(line[0])
                last_digit = int(line[-1])
                calibration_value = int(str(first_digit) + str(last_digit))     
                calibration_sum += calibration_value

    print(f"Answer: {calibration_sum}")
