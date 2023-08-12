tests/ui/traits/issue-97695-double-trivial-bound.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zinline-mir --emit=mir
// build-pass

pub trait Associate {
    type Associated;
}

pub struct Wrap<'a> {
    pub field: &'a i32,
}

pub trait Create<T> {
    fn create() -> Self;
}

pub fn oh_no<'a, T>()
where
    Wrap<'a>: Associate,
    <Wrap<'a> as Associate>::Associated: Create<T>,
{
    <Wrap<'a> as Associate>::Associated::create();
}

pub fn main() {}


