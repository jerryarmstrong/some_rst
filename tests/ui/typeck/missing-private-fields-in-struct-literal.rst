tests/ui/typeck/missing-private-fields-in-struct-literal.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod m {
    pub struct S {
        pub visible: bool,
        a: (),
        b: (),
        c: (),
        d: (),
        e: (),
    }
}

fn main() {
    let _ = m::S { //~ ERROR cannot construct `S` with struct literal syntax due to private fields
        visible: true,
        a: (),
        b: (),
    };
}


