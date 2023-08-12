tests/ui/stability-attribute/default-body-stability-ok-enables.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:default_body.rs
#![crate_type = "lib"]
#![feature(fun_default_body, eq_default_body, constant_default_body)]

extern crate default_body;

use default_body::{Equal, JustTrait};

struct Type;

impl JustTrait for Type {}

impl Equal for Type {
    fn neq(&self, other: &Self) -> bool {
        false
    }
}


