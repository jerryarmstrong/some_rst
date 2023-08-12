tests/ui/structs-enums/module-qualified-struct-destructure.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

mod m {
    pub struct S {
        pub x: isize,
        pub y: isize
    }
}

pub fn main() {
    let x = m::S { x: 1, y: 2 };
    let m::S { x: _a, y: _b } = x;
}


