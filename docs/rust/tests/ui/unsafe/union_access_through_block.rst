tests/ui/unsafe/union_access_through_block.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#[derive(Copy, Clone)]
pub struct Foo { a: bool }

pub union Bar {
    a: Foo,
    b: u32,
}
pub fn baz(mut bar: Bar) {
    unsafe {
        { bar.a }.a = true;
    }
}

fn main() {}


