tests/ui/traits/inheritance/auxiliary/auto_xc.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Foo { fn f(&self) -> isize; }
pub trait Bar { fn g(&self) -> isize; }
pub trait Baz { fn h(&self) -> isize; }

pub trait Quux: Foo + Bar + Baz { }

impl<T:Foo + Bar + Baz> Quux for T { }


