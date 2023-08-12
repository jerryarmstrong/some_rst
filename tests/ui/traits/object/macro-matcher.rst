tests/ui/traits/object/macro-matcher.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `ty` matcher accepts trait object types

macro_rules! m {
    ($t: ty) => ( let _: $t; )
}

fn main() {
    m!(dyn Copy + Send + 'static);
    //~^ ERROR the trait `Copy` cannot be made into an object
    m!(dyn 'static + Send);
    m!(dyn 'static +); //~ ERROR at least one trait is required for an object type
}


