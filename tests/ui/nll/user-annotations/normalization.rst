tests/ui/nll/user-annotations/normalization.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we enforce a `&'static` requirement that is only visible
// after normalization.

trait Foo { type Out; }
impl Foo for () { type Out = &'static u32; }
impl<'a> Foo for &'a () { type Out = &'a u32; }

fn main() {
    let a = 22;
    let _: <() as Foo>::Out = &a; //~ ERROR

    let a = 22;
    let _: <&'static () as Foo>::Out = &a; //~ ERROR

    let a = 22;
    let _: <&'_ () as Foo>::Out = &a;
}


