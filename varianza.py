def print_grades(grades):
    for grade in grades:
        print(grade)


def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = float(sum_of_grades) / len(grades)
    return average


#Para calcular la varianza restamos a cada puntancion la media y los sumamos, lo elevamos al cuadrado y lo divimos entre 2
def grades_variance(scores, average):
    sumatorio = 0
    for data in scores:
        sumatorio += (average - float(data)) ** 2
    variance = float(sumatorio) / len(grades)
    return variance


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("La varianza es:",grades_variance(grades, grades_average(grades)))