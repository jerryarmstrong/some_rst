tests/ui/specialization/issue-50452-fail.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)]
//~^ WARN the feature `specialization` is incomplete

pub trait Foo {
    fn foo();
}

impl Foo for i32 {}
impl Foo for i64 {
    fn foo() {}
    //~^ERROR `foo` specializes an item from a parent `impl`
}
impl<T> Foo for T {
    fn foo() {}
}

fn main() {
    i32::foo();
    i64::foo();
    u8::foo();
}


