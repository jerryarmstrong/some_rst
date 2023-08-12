tests/ui/resolve/missing-in-namespace.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _map = std::hahmap::HashMap::new();
    //~^ ERROR failed to resolve: could not find `hahmap` in `std
}


