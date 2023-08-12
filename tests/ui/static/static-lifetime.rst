tests/ui/static/static-lifetime.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Arbitrary: Sized + 'static {}

impl<'a, A: Clone> Arbitrary for ::std::borrow::Cow<'a, A> {} //~ ERROR lifetime bound

fn main() {
}


