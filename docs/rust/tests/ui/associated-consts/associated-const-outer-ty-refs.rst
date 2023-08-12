tests/ui/associated-consts/associated-const-outer-ty-refs.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Lattice {
    const BOTTOM: Self;
}

impl<T> Lattice for Option<T> {
    const BOTTOM: Option<T> = None;
}

fn main(){}


