tests/ui/stability-attribute/default-body-stability-ok-impls.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:default_body.rs
#![crate_type = "lib"]

extern crate default_body;

use default_body::{Equal, JustTrait};

struct Type;

impl JustTrait for Type {
    const CONSTANT: usize = 1;

    fn fun() {}
}

impl Equal for Type {
    fn eq(&self, other: &Self) -> bool {
        false
    }
}


