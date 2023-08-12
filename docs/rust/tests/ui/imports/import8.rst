tests/ui/imports/import8.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use foo::x;
use foo::x as z;

mod foo {
    pub fn x(y: isize) { println!("{}", y); }
}

pub fn main() { x(10); z(10); }


