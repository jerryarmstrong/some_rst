tests/ui/traits/bound/auxiliary/on_structs_and_enums_xc.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Trait {
    fn dummy(&self) { }
}

pub struct Foo<T:Trait> {
    pub x: T,
}

pub enum Bar<T:Trait> {
    ABar(isize),
    BBar(T),
    CBar(usize),
}


