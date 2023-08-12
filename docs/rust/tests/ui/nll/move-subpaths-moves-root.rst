tests/ui/nll/move-subpaths-moves-root.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = (vec![1, 2, 3], );
    drop(x.0);
    drop(x); //~ ERROR use of partially moved value
}


