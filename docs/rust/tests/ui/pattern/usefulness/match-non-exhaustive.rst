tests/ui/pattern/usefulness/match-non-exhaustive.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match 0 { 1 => () } //~ ERROR non-exhaustive patterns
    match 0 { 0 if false => () } //~ ERROR non-exhaustive patterns
}


