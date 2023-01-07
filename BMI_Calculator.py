def bmi_calculator(weight, height):
    total_bmi = ((703 * weight) / (height ** 2))
    return total_bmi

def bmi_classification(bmi):
    if bmi < 18.5:
        return 'Underweight'
    if 18.5 < bmi < 24.99:
        return 'Normal Weight'
    if 25 < bmi < 29.99:
        return 'Overweight'
    if 30 < bmi < 34.99:
        return 'Obese(Class 1)'
    if 35 < bmi < 39.99:
        return 'Obese(Class 2)'
    if bmi > 40:
        return 'Morbidly Obese'

def main():

    while True:
        weight = int(input('Enter weight in lbs: '))
        if weight < 0:
            print('Weight must be positive number.')
            continue
        else:
            break
    while True:
        height = int(input('Enter height in Inches: '))
        if height < 0:
            print('Height must be a positive number.')
            continue
        else:
            break
    print()
    total = bmi_calculator(weight, height)
    bmi = bmi_classification(total)
    print(f'Your total bmi is: {total: .2f}')
    print(f'Your classification is: {bmi}')
    while True:
        print()
        answer = input('Compute BMI for another person? (y/n): ').lower()
        print()
        if answer == 'y':
            main()
        if answer == 'n':
            print('Thank you for using BMI Calculator.')
            break
        break

main()