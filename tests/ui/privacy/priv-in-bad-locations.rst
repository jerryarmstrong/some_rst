tests/ui/privacy/priv-in-bad-locations.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub extern "C" { //~ ERROR unnecessary visibility qualifier
    pub fn bar();
}

trait A {
    fn foo(&self) {}
}

struct B;

pub impl B {} //~ ERROR unnecessary visibility qualifier

pub impl A for B { //~ ERROR unnecessary visibility qualifier
    pub fn foo(&self) {} //~ ERROR unnecessary visibility qualifier
}

pub fn main() {}


