tests/ui/const-generics/infer/uninferred-consts.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we emit an error if we cannot properly infer a constant.

// taken from https://github.com/rust-lang/rust/issues/70507#issuecomment-615268893
struct Foo;
impl Foo {
    fn foo<const A: usize, const B: usize>(self) {}
}
fn main() {
    Foo.foo();
    //~^ ERROR type annotations needed
}


