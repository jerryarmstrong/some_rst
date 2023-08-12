tests/ui/imports/double-import.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This tests that conflicting imports shows both `use` lines
// when reporting the error.

mod sub1 {
    pub fn foo() {} // implementation 1
}

mod sub2 {
    pub fn foo() {} // implementation 2
}

use sub1::foo;
use sub2::foo; //~ ERROR the name `foo` is defined multiple times

fn main() {}


