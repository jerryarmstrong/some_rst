src/tools/miri/tests/pass/trivial.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn empty() {}

fn unit_var() {
    let x = ();
    x
}

fn main() {
    empty();
    unit_var();
}


