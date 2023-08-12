tests/ui/compare-method/region-extra.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that you cannot add an extra where clause in the impl relating
// two regions.

trait Master<'a, 'b> {
    fn foo();
}

impl<'a, 'b> Master<'a, 'b> for () {
    fn foo() where 'a: 'b { } //~ ERROR impl has stricter
}

fn main() {
    println!("Hello, world!");
}


