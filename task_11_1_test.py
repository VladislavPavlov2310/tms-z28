import task_11_1 as tsk

# AppsFromStore
app1 = tsk.AppsFromStore('shooter', 145, 4.5)
print(app1)
app1.write_review()
print(app1)
print('\n')

# Workers
worker1 = tsk.Worker('Andrei', 'Smirnov', 4)
print(worker1)
worker1.calc_salary()
worker1.calc_tax()
print(worker1)
print('\n')

# RepairElectronics
electr1 = tsk.RepairElectronics('notebook', 'broken keyboard', 5)
print(electr1)
print(electr1.fix_cost())
electr1.fix()
print(electr1)
print('\n')

# Weapon
gun1 = tsk.Weapon('pistol', 0.3, 5)
print(gun1)
gun1.shot()
gun1.reload()
print('\n')

# Pet
pet1 = tsk.Pet('Alabai', 2, 1.0)
print(pet1)
pet1.walk()
pet1.eat()
