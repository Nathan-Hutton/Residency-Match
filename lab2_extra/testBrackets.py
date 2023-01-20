'''
Created on Aug 17, 2018
Modified on Aug 28, 2022
@auther: Jingsai Liang
'''

import Brackets

def testBrackets():
    result = Brackets.Brackets('')
    assert result

    result = Brackets.Brackets('()')
    assert result

    result = Brackets.Brackets('([]){}')
    assert result

    result = Brackets.Brackets('(((((([[]]{}))))))')
    assert result

    result = Brackets.Brackets('[([{()}])]')
    assert result

    result = Brackets.Brackets(']')
    assert not result

    result = Brackets.Brackets('[][')
    assert not result

    result = Brackets.Brackets('()((])')
    assert not result

    result = Brackets.Brackets('((())')
    assert not result

    result = Brackets.Brackets('([{}]]')
    assert not result

    result = Brackets.Brackets('{{{}}}}')
    assert not result
