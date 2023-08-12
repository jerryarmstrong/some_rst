tests/ui/let-else/let-else-binding-immutable.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // from rfc2005 test suite



pub fn main() {
    let Some(x) = &Some(3) else {
        panic!();
    };
    *x += 1; //~ ERROR: cannot assign to `*x`, which is behind a `&` reference
}


