tests/ui/match/match-vec-mismatch-2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match () {
        [()] => { }
        //~^ ERROR expected an array or slice, found `()`
    }
}


