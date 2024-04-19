import pytest
from Stack import Stack


@pytest.mark.parametrize(
    'instr, expected',
    (
        ['(((([{}]))))', 'Сбалансированно'],
        ['[([])((([[[]]])))]{()}', 'Сбалансированно'],
        ['{{[()]}}', 'Сбалансированно'],
        ['}{}', 'Несбалансированно'],
        ['{{[(])]}}', 'Несбалансированно'],
        ['[[{())}]', 'Несбалансированно'],
    )
)
def test_main(instr, expected):
    st = Stack(instr)
    assert st.check() == expected