tests/ui/consts/qualif_overwrite_2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::Cell;

// const qualification is not smart enough to know about fields and always assumes that there might
// be other fields that caused the qualification
const FOO: &Option<Cell<usize>> = {
    let mut a = (Some(Cell::new(0)),);
    a.0 = None; // sets `qualif(a)` to `qualif(a) | qualif(None)`
    &{a.0} //~ ERROR cannot refer to interior mutable
};

fn main() {}


