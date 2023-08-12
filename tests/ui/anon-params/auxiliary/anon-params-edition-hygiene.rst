tests/ui/anon-params/auxiliary/anon-params-edition-hygiene.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2015

#[macro_export]
macro_rules! generate_trait_2015 {
    ($Type: ident) => {
        trait Trait {
            fn method($Type) {}
        }
    };
}

fn main() {}


