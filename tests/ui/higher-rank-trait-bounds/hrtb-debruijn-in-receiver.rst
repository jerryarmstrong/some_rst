tests/ui/higher-rank-trait-bounds/hrtb-debruijn-in-receiver.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the case where the `Self` type has a bound lifetime that must
// be adjusted in the fn signature. Issue #19537.

use std::collections::HashMap;

struct Foo<'a> {
    map: HashMap<usize, &'a str>
}

impl<'a> Foo<'a> {
    fn new() -> Foo<'a> { panic!() }
    fn insert(&'a mut self) { }
}
fn main() {
    let mut foo = Foo::new();
    foo.insert();
    foo.insert(); //~ ERROR cannot borrow
}


