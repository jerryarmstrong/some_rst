tests/ui/binding/const-param.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Identifier pattern referring to a const generic parameter is an error (issue #68853).

fn check<const N: usize>() {
    match 1 {
        N => {} //~ ERROR const parameters cannot be referenced in patterns
        _ => {}
    }
}

fn main() {}


