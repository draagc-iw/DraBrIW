from DraBrIW.BaseBrew import Brew, BrewDecorator
from DraBrIW.Brews import Americano


def test_brew_abstract():
    try:
        a = Brew()
        b = BrewDecorator(a)
    except TypeError:
        assert True
    else:
        assert False
