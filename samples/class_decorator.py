from chaps import SINGLETON_SCOPE, Container, inject, scope


@inject('heater', 'pump')
class CoffeeMaker(object):
    def make_coffee(self):
        return "heater: %r\npump: %r" % (self.heater, self.pump)


@inject('extra_pump')
class Heater(object):
    def __repr__(self):
        return '<Heater id=%s\nextra_pump=%r>' % (
            id(self), self.extra_pump)


@inject('heater')
class Pump(object):
    def __repr__(self):
        return '<Pump id=%s heater=%r>' % (id(self), self.heater)


@scope(SINGLETON_SCOPE)  # Only one instance is managed for whole application
class ExtraPump(object):
    def __repr__(self):
        return '<ExtraPump id=%s>' % (id(self),)


Container.configure({
    'heater': Heater,
    'pump': Pump,
    'extra_pump': ExtraPump
})

if __name__ == '__main__':
    print(CoffeeMaker().make_coffee())

    # Ouput
    # heater: <Heater id=140440945316584
    # extra_pump=<ExtraPump id=140440945316696>>
    # pump: <Pump id=140440945316640 heater=<Heater id=140440945316808
    # extra_pump=<ExtraPump id=140440945316696>>>