tests/ui/parser/pat-tuple-3.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match (0, 1, 2) {
        (.., pat, ..) => {}
        //~^ ERROR `..` can only be used once per tuple pattern
    }
}


