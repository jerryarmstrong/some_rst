tests/ui/resolve/resolve-variant-assoc-item.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum E { V }
use E::V;

fn main() {
    E::V::associated_item; //~ ERROR failed to resolve: `V` is a variant, not a module
    V::associated_item; //~ ERROR failed to resolve: `V` is a variant, not a module
}


