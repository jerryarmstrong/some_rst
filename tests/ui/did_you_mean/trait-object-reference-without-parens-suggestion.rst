tests/ui/did_you_mean/trait-object-reference-without-parens-suggestion.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(bare_trait_objects)]

fn main() {
    let _: &Copy + 'static; //~ ERROR expected a path
    //~^ ERROR cannot be made into an object
    let _: &'static Copy + 'static; //~ ERROR expected a path
}


