tests/ui/match/single-line.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = match Some(42) { Some(x) => x, None => "" }; //~ ERROR E0308
}


