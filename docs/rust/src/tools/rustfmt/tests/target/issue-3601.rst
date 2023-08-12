src/tools/rustfmt/tests/target/issue-3601.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_generics)]

trait A {
    fn foo(&self);
}

pub struct B<const N: usize>([usize; N]);

impl<const N: usize> A for B<{ N }> {
    fn foo(&self) {}
}


