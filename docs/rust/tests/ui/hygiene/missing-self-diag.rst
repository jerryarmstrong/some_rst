tests/ui/hygiene/missing-self-diag.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #66898
// Tests that we don't emit a nonsensical error message
// when a macro invocation tries to access `self` from a function
// that has a 'self' parameter

pub struct Foo;

macro_rules! call_bar {
    () => {
        self.bar(); //~ ERROR expected value
    }
}

impl Foo {
    pub fn foo(&self) {
        call_bar!();
    }

    pub fn bar(&self) {
    }
}

fn main() {}


