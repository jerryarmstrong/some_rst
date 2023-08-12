tests/ui/lint/lint-unnecessary-import-braces.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_import_braces)]

use test::{A}; //~ ERROR braces around A is unnecessary

mod test {
    use test::{self}; // OK
    use test::{self as rename}; // OK
    pub struct A;
}

fn main() {}


