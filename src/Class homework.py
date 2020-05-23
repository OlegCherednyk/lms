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

    def intersect(self, point):
        if math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2) < self.rad:
            return True
        else:
            return False


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
            return True
        else:
            return False


class Train(Transport):
    def __init__(self, mas, color, m_speed, intercity=False):
        super().__init__(mas, color, m_speed)
        self.intercity = intercity

    def check_intercity(self):
        if self.check_speed():
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


class DescriptorRange:
    def __init__(self, name, min_value, max_value, initval=None):
        self.val = initval
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, obj , objtype):
        return obj.__dict__[self.name]

    def __set__(self, obj, val):
        if val < self.min_value or val > self.max_value:
            raise ValueError("Значение не входит в диапазон")
        else:
            self.val = val
            obj.__dict__[self.name] = val

    def __del__(self):
        self.val = None


class Typed(DescriptorRange):
    type_ = object

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('Expected %s' % self.type_)
        super().__set__(instance, value)


class Integer(Typed):
    type_ = int


class Float(Typed):
    type_ = float


class RangeInteger(Integer, DescriptorRange):
    pass


class RangeFloat(Float, DescriptorRange):
    pass


class Employee:

    kpi_score = RangeInteger(name='kpi_score', min_value=0, max_value=100)
    kpi_score2 = RangeFloat(name='kpi_score2', min_value=0, max_value=100)

    def __init__(self, first_name=None, last_name=None, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def __bool__(self):
        return bool(self._first_name or \
                    self._last_name or \
                    self._email)


e = Employee()
e.kpi_score = 100
e.kpi_score2 = 99.9

def once(f):
    def fun(*args, **kwargs):

        if not hasattr(fun, '_try'):
            fun._try = 1
            fun.result = f()

        else:
            fun.result = fun.result
        return fun.result
    return fun


@once
def get_logger():
    return [1, 2, 3] * 2


assert id(get_logger()) == id(get_logger()), "Not equal"
print('SUCCESS!')
