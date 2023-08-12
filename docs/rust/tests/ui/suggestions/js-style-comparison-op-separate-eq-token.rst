tests/ui/suggestions/js-style-comparison-op-separate-eq-token.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    if 1 == = 1 { //~ ERROR expected expression
        println!("yup!");
    }
}


