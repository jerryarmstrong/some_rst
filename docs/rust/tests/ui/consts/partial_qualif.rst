tests/ui/consts/partial_qualif.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::Cell;

const FOO: &(Cell<usize>, bool) = {
    let mut a = (Cell::new(0), false);
    a.1 = true; // sets `qualif(a)` to `qualif(a) | qualif(true)`
    &{a} //~ ERROR cannot refer to interior mutable
};

fn main() {}


