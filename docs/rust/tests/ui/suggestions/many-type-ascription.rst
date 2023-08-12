tests/ui/suggestions/many-type-ascription.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = 0: i32; //~ ERROR: type ascription is experimental
    let _ = 0: i32; // (error only emitted once)
}


