tests/ui/traits/default-method/supervtable.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


// Tests that we can call a function bounded over a supertrait from
// a default method

fn require_y<T: Y>(x: T) -> isize { x.y() }

trait Y {
    fn y(self) -> isize;
}


trait Z: Y + Sized {
    fn x(self) -> isize {
        require_y(self)
    }
}

impl Y for isize {
    fn y(self) -> isize { self }
}

impl Z for isize {}

pub fn main() {
    assert_eq!(12.x(), 12);
}


