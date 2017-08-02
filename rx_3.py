import rx
from rx import Observable, Observer
from rx.testing import marbles
from rx.subjects import Subject


class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)

    def on_error(self, e):
        print("Got error: %s" % e)

    def on_completed(self):
        print("Sequence completed")


# xs = Observable.from_iterable(range(10))
# d = xs.subscribe(MyObserver())
# xs = Observable.from_(range(10))
# d = xs.subscribe(print)

def main():
    stream = Subject()
    stream.on_next(41)

    d = stream.subscribe(lambda x: print("Got: %s" % x))

    stream.on_next(42)

    d.dispose()
    stream.on_next(43)


    xs = Observable.from_marbles("1-x-3-4-5")
    ys = Observable.from_marbles("1-2-3-4-5")

    print(xs.merge(ys).to_blocking().to_marbles())



    xs = Observable.from_marbles("a-b-c-|")
    xs.to_blocking().to_marbles()


    xs = Observable.range(1, 5)
    ys = Observable.from_("abcde")
    zs = xs.merge(ys).subscribe(print)


    xs = Observable.from_(range(10, 20, 2))
    d = xs.map(
        lambda x, i: "%s: %s" % (i, x * 2)
    ).subscribe(print)

    return


if __name__ == "__main__":

    main()