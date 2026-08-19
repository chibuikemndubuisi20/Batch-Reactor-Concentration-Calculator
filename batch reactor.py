
import math

times = []
concentrations = []

print("Reaction order")
print("1 = first order")
print("2 = second order")
print("3 = third order")

order = input("What is the reaction order (Use numbers)? ")
initial_conc = float(input("What is the initial concentration in mol/dm^3? "))
rate_cons = float(input("What is the rate constant? "))
max_time = int(input("What is the maximum reaction time in minutes? "))


def first_order(initial_conc, rate_cons, time):
    concentration = initial_conc * math.exp((-1 * rate_cons) * time)
    return concentration


def second_order(initial_conc, rate_cons, time):
    concentration = 1 / ((1 / initial_conc) + (rate_cons * time))
    return concentration


def third_order(initial_conc, rate_cons, time):
    concentration = 1 / math.sqrt((1 / (initial_conc ** 2)) + (2 * rate_cons * time))
    return concentration


if order == "1":
    for i in range(0, max_time + 1):
        concentration = first_order(initial_conc, rate_cons, i)
        times.append(i)
        concentrations.append(concentration)
        print("The concentration when the time is " + str(i) + " min is " + str(concentration) + " mol/dm^3 .")


elif order == "2":
    for i in range(0, max_time + 1):
        concentration = second_order(initial_conc, rate_cons, i)
        times.append(i)
        concentrations.append(concentration)
        print("The concentration when the time is " + str(i) + " min is " + str(concentration) + " mol/dm^3.")


elif order == "3":
    for i in range(0, max_time + 1):
        concentration = third_order(initial_conc, rate_cons, i)
        times.append(i)
        concentrations.append(concentration)
        print("The concentration when the time is " + str(i) + " min is " + str(concentration) + " mol/dm^3.")

print(times)
print(concentrations)
