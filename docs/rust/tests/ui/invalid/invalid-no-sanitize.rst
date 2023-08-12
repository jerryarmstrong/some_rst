tests/ui/invalid/invalid-no-sanitize.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(no_sanitize)]

#[no_sanitize(brontosaurus)] //~ ERROR invalid argument
fn main() {
}


