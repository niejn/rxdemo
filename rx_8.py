
import multiprocessing
import random
import time
from logging import log
from threading import current_thread

# from jupyter_core.troubleshoot import subs
from rx import Observable as O
from rx.concurrency import ThreadPoolScheduler, new_thread_scheduler
import threading
from rx.linq.observable import merge, subscribeon
import multiprocessing
import random
import time
from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler
def emit(obs):
    for i in range(0, 10):
        log('emitting', i, obs.__class__.__name__, hash(obs))
        # going nowhere
        obs.on_next(i)
        time.sleep(0.1)

ts_glob = 0 # global start time
class Subscriber:
    def __init__(self, observed_stream, **kw):
        print ('')
        name = kw.get('name', str(hash(self))[-5:])
        log('New subscription (%s) on stream' % str(name).strip(),
             hash(observed_stream))
        self.ts = time.time() # tstart, for dts at events
        # no postifx after name, sometimes it ends with '\n':
        self.name = name

    def _on(self, what, v=''):
        print ('%s %s [%s] %s: %s -> %s' % (
                dt(ts_glob), cur_thread(), what, dt(self.ts), v, self.name))

    def on_next     (self, v): return self._on('next', v)
    def on_error    (self, v): return self._on('err ', v)
    def on_completed(self)   : return self._on('cmpl', 'fin')


def subs(src, **kw):
    # required for e.g. .multicast:
    obs = Subscriber(src, **kw)
    disposable = src.subscribe(obs)
    if kw.pop('return_subscriber', None):
        return disposable, obs
    return disposable


published = O.create(emit).publish()




threading._start_new_thread(published.connect, ())
time.sleep(0.5)
d = subscribe(published, scheduler=new_thread_scheduler)