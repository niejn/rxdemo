from rx import Observable
from random import randint

# Observable.merge(), Observable.concat(), Observable.zip(), and Observable.combine_latest()

letters = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

intervals = Observable.interval(1000)

Observable.zip(letters, intervals, lambda s, i: (s, i)) \
    .subscribe(lambda t: print(t))

input("Press any key to quit\n")


three_emissions = Observable.range(1, 3)

three_random_ints = three_emissions.map(lambda i: randint(1, 100000)).publish().auto_connect(2)
# three_random_ints = three_emissions.map(lambda i: randint(1, 100000)).publish().connect()
three_random_ints.subscribe(lambda i: print("Subscriber 1 Received: {0}".format(i)))
three_random_ints.subscribe(lambda i: print("Subscriber 2 Received: {0}".format(i))) # second subscriber triggers firing


three_emissions = Observable.range(1, 3)

three_random_ints = three_emissions.map(lambda i: randint(1, 100000)).publish()

three_random_ints.subscribe(lambda i: print("Subscriber 1 Received: {0}".format(i)))
three_random_ints.subscribe(lambda i: print("Subscriber 2 Received: {0}".format(i)))

three_random_ints.connect()



three_emissions = Observable.range(1, 3)

three_random_ints = three_emissions.map(lambda i: randint(1, 100000))

three_random_ints.subscribe(lambda i: print("Subscriber 1 Received: {0}".format(i)))
three_random_ints.subscribe(lambda i: print("Subscriber 2 Received: {0}".format(i)))