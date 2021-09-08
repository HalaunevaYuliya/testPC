day_1 = {
        'Cardio':'30 minutes with 2-3 breaks',
        'push-ups':'from the bench 3 sets of 15 repetitions',
        'hyperextension':'3 sets of 25 reps',
        'biceps':'curl in the simulator - 3 sets of 15-20 reps',
        'crossover':'3 sets of 15 reps',
        'press':'2-3 exercises without interruption'
}

day_2 = {
        'interval_cardio':'20 minutes',
        'legs':'Barbell Squat - 3 sets of 15 reps',
        'arms':'Extension in a crossover with a rope - 3 sets of 20 reps',
        'flexion':'flexion/extension of the legs in the simulator - 3 sets of 15-20 reps',
        'breeding':'light dumbbells through the sides - 3 sets of 15 reps',
        'jogging':'20 minutes'
}

day_3 = {
        'interval_cardio':'20 minutes',
        'hyperextension':'3 sets of 25 reps',
        'deadlift':'4 sets of 20 reps',
        'lift':'upper block - 4 sets of 20 reps',
        'incline':'dumbbell breeding - 3 sets of 20 reps',
        'Flexion':'hands with dumbbells - 3 sets of 20 reps'
}
training_dict = {'day1':day_1, 'day2':day_2, 'day3':day_3}

print('План тренировки в тренажерном зале, расчитанный на 3 тренировки в неделю')
print('1 - Просмотр недельного плана')
print('2 - Добавить дополнительную тренировку в бассейне')
print('3 - Удалить тренировочный день')
print('4 - Вывести отдельный тренировочный день')
print('0 - Для выхода из программы')
x = ''
while x != 0:
        x = int(input('Сделайте выбор: 1, 2, 3, 4 или 0  '))
        if x == 1:
                for i in training_dict:
                        print(f'{i}')
                        for ii in training_dict[i]:
                               print(f'{ii} - {training_dict[i][ii]}')
        elif x == 2:
                training_dict['day_4'] = {'swimming': '35 min'}



