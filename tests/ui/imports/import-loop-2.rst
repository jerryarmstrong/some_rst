tests/ui/imports/import-loop-2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:import

mod a {
    pub use b::x;
}

mod b {
    pub use a::x;

    fn main() { let y = x; }
}

fn main() {}


