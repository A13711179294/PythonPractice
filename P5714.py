weight, height = map(float, input().split())
BMI = weight / (height * height)
if BMI < 18.5:
    print('Underweight')
elif 24 > BMI >= 18.5:
    print('Normal')
else:
    print('%.6g' % BMI)
    print('Overweight')
