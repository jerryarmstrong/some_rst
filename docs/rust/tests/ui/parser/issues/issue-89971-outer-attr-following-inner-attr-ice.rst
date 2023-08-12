tests/ui/parser/issues/issue-89971-outer-attr-following-inner-attr-ice.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:issue-89971-outer-attr-following-inner-attr-ice.rs

#[macro_use]
extern crate issue_89971_outer_attr_following_inner_attr_ice;

fn main() {
    Mew();
    X {};
}

#![deny(missing_docs)]
//~^ ERROR an inner attribute is not permitted in this context
#[derive(ICE)]
#[deny(missing_docs)]
struct Mew();


