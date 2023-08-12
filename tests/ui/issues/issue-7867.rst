tests/ui/issues/issue-7867.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum A { B, C }

mod foo { pub fn bar() {} }

fn main() {
    match (true, false) {
        A::B => (),
        //~^ ERROR mismatched types
        //~| expected tuple, found enum `A`
        //~| expected tuple `(bool, bool)`
        //~| found enum `A`
        _ => ()
    }
}


