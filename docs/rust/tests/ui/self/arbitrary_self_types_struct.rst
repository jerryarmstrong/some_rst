tests/ui/self/arbitrary_self_types_struct.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::rc::Rc;

struct Foo {
    x: i32,
    y: i32,
}

impl Foo {
    fn x(self: &Rc<Self>) -> i32 {
        self.x
    }

    fn y(self: Rc<Self>) -> i32 {
        self.y
    }
}

fn main() {
    let foo = Rc::new(Foo {x: 3, y: 4});
    assert_eq!(3, foo.x());
    assert_eq!(4, foo.y());
}


