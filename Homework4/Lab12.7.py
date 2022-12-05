# JenniferChu
# 1873159

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.\nCould not calculate heart rate info.\n')
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        calculate_hr = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age, 'year-old:', calculate_hr, 'bpm')
    except ValueError:
        print("Invalid age.\nCould not calculate heart rate info.\n")
