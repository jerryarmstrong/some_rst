tests/rustdoc-ui/check-doc-alias-attr-location.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Bar;
pub trait Foo {
    type X;
    fn foo() -> Self::X;
}

#[doc(alias = "foo")] //~ ERROR
extern "C" {}

#[doc(alias = "bar")] //~ ERROR
impl Bar {
    #[doc(alias = "const")]
    pub const A: u32 = 0;
}

#[doc(alias = "foobar")] //~ ERROR
impl Foo for Bar {
    #[doc(alias = "assoc")] //~ ERROR
    type X = i32;
    fn foo() -> Self::X {
        0
    }
}


