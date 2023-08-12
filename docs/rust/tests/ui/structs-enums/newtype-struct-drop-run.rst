tests/ui/structs-enums/newtype-struct-drop-run.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Make sure the destructor is run for newtype structs.

use std::cell::Cell;

struct Foo<'a>(&'a Cell<isize>);

impl<'a> Drop for Foo<'a> {
    fn drop(&mut self) {
        let Foo(i) = *self;
        i.set(23);
    }
}

pub fn main() {
    let y = &Cell::new(32);
    {
        let _x = Foo(y);
    }
    assert_eq!(y.get(), 23);
}


