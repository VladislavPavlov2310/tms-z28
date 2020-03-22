import task_12_2 as tsk


def add_figure(fgr_list):
    choice = int(input('1) Add circle\n2) Add triangle\n3) Add square\n'))
    if choice == 1:
        fgr_list.append(tsk.Circle(tsk.Point(int(input('Input x for center: ')), int(input('Input y for center: '))),
                                   int(input('Input radius: '))))
    elif choice == 2:
        fgr_list.append(tsk.Triangle(tsk.Point(int(input('Input x for point 1 ')), int(input('Input y for point 1 '))),
                                     tsk.Point(int(input('Input x for point 2 ')), int(input('Input y for point 2 '))),
                                     tsk.Point(int(input('Input x for point 3 ')), int(input('Input y for point 3 ')))))
    elif choice == 3:
        fgr_list.append(tsk.Square(tsk.Point(int(input('Input x for point 1 ')), int(input('Input y for point 1 '))),
                                   tsk.Point(int(input('Input x for point 2 ')), int(input('Input y for point 2 ')))))


# circle1 = tsk.Circle(tsk.Point(2, 3), 5)
# print(circle1)
# triangle1 = tsk.Triangle(tsk.Point(2, 2), tsk.Point(5, 5), tsk.Point(8, 0))
# print(triangle1)
# square1 = tsk.Square(tsk.Point(1, 1), tsk.Point(6, 6))
# print(square1)


figure_list = []
while True:
    add_figure(figure_list)
    ch = input('Do you want to add next figure? (y/n)')
    if ch != 'y':
        break
for index, elem in enumerate(figure_list):
    print(f'{index + 1})\n{elem.square}')

