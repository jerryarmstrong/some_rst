tests/ui/macros/malformed_macro_lhs.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! my_precioooous {
    t => (1); //~ ERROR invalid macro matcher
}

fn main() {
    my_precioooous!();
}


