tests/ui/user-defined-macro-rules.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! macro_rules { () => { struct S; } } // OK

macro_rules! {} // OK, calls the macro defined above

fn main() {
    let s = S;
}


