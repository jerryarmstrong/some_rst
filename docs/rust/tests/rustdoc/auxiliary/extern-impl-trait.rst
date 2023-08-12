tests/rustdoc/auxiliary/extern-impl-trait.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Foo {
    type Associated;
}

pub struct X;
pub struct Y;


impl Foo for X {
    type Associated = ();
}

impl Foo for Y {
    type Associated = ();
}

impl X {
    pub fn returns_sized<'a>(&'a self) -> impl Foo<Associated=()> + 'a {
        X
    }
}

impl Y {
    pub fn returns_unsized<'a>(&'a self) -> Box<impl ?Sized + Foo<Associated=()> + 'a> {
        Box::new(X)
    }
}


