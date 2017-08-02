from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler
import rx.linq.observable.select

rx.linq.observable.select.reset_start_time(O.map, title='map') # alias is "select"
# warming up:
d = rx.linq.observable.select.subs(O.from_((1, 2 , 3)).map(lambda x: x * 2))


rx.linq.observable.pluck

rst(O.pluck, title='pluck')
d = subs(O.from_([{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]).pluck('y'))

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
rst(title='pluck_attr')
d = subs(O.from_([Coord(1, 2), Coord(3, 4)]).pluck_attr('y'))






rst(O.flat_map)
stream = O.range(1, 2)\
           .flat_map(lambda x: O.range(x, 2)) # alias: select_many
d = subs(stream)






rst() # from an array
s1 = O.from_(('a', 'b', 'c'))
d  = subs(s1.flat_map(lambda x: x))
d  = subs(s1.flat_map(lambda x, i: (x, i)))
#d = subs(O.from_(('a', 'b', 'c')).flat_map(lambda x, i: '%s%s' % (x, i))) # ident, a string is iterable

header('using a result selector')

def res_sel(*a):
    # in conrast to the RxJS example I get only 3 parameters, see output
    return '-'.join([str(s) for s in a])

# for every el of the original stream we get *additional* two elements: the el and its index:
d = subs(s1.flat_map(lambda x, i: (x, i)         , res_sel))
# ident, flat_map flattens the inner stream:
d = subs(s1.flat_map(lambda x, i: O.from_((x, i)), res_sel))



rst(O.for_in)
abc = O.from_marbles('a-b|').to_blocking()

# abc times 3, via:
d = subs(O.for_in([1, 2, 3],
                  lambda i: abc.map(
                      # just to get the results of array and stream:
                      lambda letter: '%s%s' % (letter, i) )))
sleep(0.5)
# we can also for_in from an observable.
# TODO: Dont' understand the output though - __doc__ says only arrays.
d = subs(O.for_in(O.from_((1, 2, 3)),
                  lambda i: abc.map(lambda letter: '%s%s' % (letter, i) )).take(2))