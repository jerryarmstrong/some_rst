tests/ui/consts/const_let_assign3.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    state: u32,
}

impl S {
    const fn foo(&mut self, x: u32) {
        //~^ ERROR mutable reference
        self.state = x;
    }
}

const FOO: S = {
    let mut s = S { state: 42 };
    s.foo(3); //~ ERROR mutable reference
    s
};

type Array = [u32; {
    let mut x = 2;
    let y = &mut x; //~ ERROR mutable reference
    *y = 42;
    *y
}];

fn main() {
    assert_eq!(FOO.state, 3);
}


