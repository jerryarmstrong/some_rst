tests/ui/macros/macro-expanded-include/test.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// build-pass (FIXME(62277): could be check-pass?)
#![allow(unused)]

#[macro_use]
mod foo;

m!();
fn f() {
    n!();
}

fn main() {}


