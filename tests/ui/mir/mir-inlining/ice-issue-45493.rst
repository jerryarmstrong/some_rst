tests/ui/mir/mir-inlining/ice-issue-45493.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zmir-opt-level=3

trait Array {
    type Item;
}

fn foo<A: Array>() {
    let _: *mut A::Item = std::ptr::null_mut();
}

struct Foo;
impl Array for Foo { type Item = i32; }

fn main() {
    foo::<Foo>();
}


