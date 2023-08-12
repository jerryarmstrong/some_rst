tests/ui/nll/issue-57280-1-flipped.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test should compile, as the lifetimes
// in matches don't really matter.
//
// We currently use contravariance when checking the
// type of match arms.

trait Foo<'a> {
    const C: &'a u32;
}

impl<'a, T> Foo<'a> for T {
    const C: &'a u32 = &22;
}

fn foo<'a>(x: &'static u32) {
    match x {
        <() as Foo<'a>>::C => { }
        //~^ ERROR lifetime may not live long enough
        &_ => { }
    }
}

fn main() {}


