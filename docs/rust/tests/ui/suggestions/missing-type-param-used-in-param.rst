tests/ui/suggestions/missing-type-param-used-in-param.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn two_type_params<A, B>(_: B) {}

fn main() {
    two_type_params::<String>(100); //~ ERROR function takes 2 generic arguments
    two_type_params::<String, _>(100);
}


