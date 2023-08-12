tests/ui/suggestions/suggest-add-self.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X(i32);

impl X {
    pub(crate) fn f() {
        self.0
        //~^ ERROR expected value, found module `self`
    }

    pub fn g() {
        self.0
        //~^ ERROR expected value, found module `self`
    }
}

fn main() {}


