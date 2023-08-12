tests/ui/lint/forbid-error-capped.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-args: --cap-lints=warn -Fwarnings

// This checks that the forbid attribute checking is ignored when the forbidden
// lint is capped.

#![forbid(warnings)]
#![allow(unused)]

#[allow(unused)]
mod bar {
    fn bar() {}
}

fn main() {}


