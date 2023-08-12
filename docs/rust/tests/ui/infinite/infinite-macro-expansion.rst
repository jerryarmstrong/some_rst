tests/ui/infinite/infinite-macro-expansion.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! recursive {
    () => (recursive!()) //~ ERROR recursion limit reached while expanding `recursive!`
}

fn main() {
    recursive!()
}


