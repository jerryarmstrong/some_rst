tests/ui/imports/overlapping_pub_trait.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:overlapping_pub_trait_source.rs

/*
 * This crate declares two public paths, `m::Tr` and `prelude::_`. Make sure we prefer the former.
 */
extern crate overlapping_pub_trait_source;
//~^ HELP the following trait is implemented but not in scope; perhaps add a `use` for it:
//~| SUGGESTION overlapping_pub_trait_source::m::Tr

fn main() {
    use overlapping_pub_trait_source::S;
    S.method();
    //~^ ERROR no method named `method` found for struct `S` in the current scope [E0599]
    //~| HELP items from traits can only be used if the trait is in scope
}


