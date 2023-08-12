tests/ui/type-alias-impl-trait/issue-76202-trait-impl-for-tait.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #76202
// Tests that we don't ICE when we have a trait impl on a TAIT.

// check-pass

#![feature(type_alias_impl_trait)]

trait Dummy {}
impl Dummy for () {}

type F = impl Dummy;
fn f() -> F {}

trait Test {
    fn test(self);
}

impl Test for F {
    fn test(self) {}
}

// Ok because `i32` does not implement `Dummy`,
// so it can't possibly be the hidden type of `F`.
impl Test for i32 {
    fn test(self) {}
}

fn main() {
    let x: F = f();
    x.test();
}


