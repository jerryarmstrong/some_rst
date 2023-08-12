tests/ui/typeck/while-loop-block-cond.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    while {} {}
    //~^ ERROR mismatched types [E0308]
}


