from Stack import Stack

if __name__ == '__main__':
    st = Stack('(((([{}]))))')
    print(st.check())
    st = Stack('[([])((([[[]]])))]{()}')
    print(st.check())
    st = Stack('{{[()]}}')
    print(st.check())
    st = Stack('}{}')
    print(st.check())
    st = Stack('{{[(])]}}')
    print(st.check())
    st = Stack('[[{())}]')
    print(st.check())