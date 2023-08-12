tests/ui/traits/trait-or-new-type-instead.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl<T> Option<T> {
//~^ ERROR cannot define inherent `impl` for a type outside of the crate where the type is defined
    pub fn foo(&self) { }
}

fn main() { }


