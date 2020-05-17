from time import  *
import math

import time


def timer(f):
    def func(*args, **kwargs):
        currtime = time.time()
        result = f(*args,**kwargs)
        print("Time to function : %f" %(time.time()-currtime))
        return result
    return func


class lazy_object:

    '''
    Class for deferred instantiation of objects.  Init is called
    only when the first attribute is either get or set.
    '''

    def __init__(self, callable, reset=0, *args, **kw,):
        '''
        callable -- Class of objeсt to be instantiated or function to be called
        *args -- arguments to be used when instantiating object
        **kw  -- keywords to be used when instantiating object
        '''
        self.__dict__['callable'] = callable
        self.__dict__['args'] = args
        self.__dict__['kw'] = kw
        self.__dict__['obj'] = None
        self.__dict__['reset'] = reset

    def init_obj(self):
        '''
        Instantiate object if not already done
        '''
        if self.reset == 1:
            self.__dict__['obj'] = None
            self.__dict__['reset'] = 0
        if self.obj is None:
            self.__dict__['obj'] = self.callable(*self.args, **self.kw)

    def __getattr__(self, name):
        self.init_obj()
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        self.init_obj()
        self.__dict__['reset'] = value
        setattr(self.obj, name, value)

    def __len__(self):
        self.init_obj()
        return len(self.obj)

    def __getitem__(self, idx):
        self.init_obj()
        return self.obj[idx]


class A:
    def __init__(self, num_elem):
        self.attr1 = list(range(num_elem))


#a = lazy_object(A, num_elem=10 ** 8)


@timer
def pr(q):
    print(q)


#pr(1 in a.attr1)
#pr(42 in a.attr1)

#a.reset = 1

#pr(43 in a.attr1)
#pr(42 in a.attr1)

#print(a.__dict__)


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Dot(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)


class Circle(Shape):
    def __init__(self, x, y, rad):
        super().__init__(x, y)
        self.rad = rad

    def check(self, other):
        if math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) < self.rad:
            print("Точка в окружности")
        else:
            print("Точка не в окружности")


#a = Dot(100, 3)
#b = Circle(1, 2, 5)
#b.check(a)


class Transport:
    def __init__(self, mas, color, m_speed):
        self.m_speed = m_speed
        self.mas = mas
        self.color = color

    def check_speed(self):
        if self.m_speed <= 100:
            return 'Грустно'
        else:
            return 'Не грустно'


class Train(Transport):
    def __init__(self, mas, color, m_speed, intercity=False):
        super().__init__(mas, color, m_speed)
        self.intercity = intercity

    def check_intercity(self):
        if self.check_speed() == 'Грустно':
            self.intercity = False


class Plane(Transport):
    def __init__(self, mas, color, m_speed, m_peoples):
        super().__init__(mas, color, m_speed)
        self.m_peoples = m_peoples

    def check_peoples(self):
        if self.m_peoples >= 800:
            print("Большой самолет")
        else:
            print("Не очень большой самолет")
