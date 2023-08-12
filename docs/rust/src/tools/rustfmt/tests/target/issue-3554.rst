src/tools/rustfmt/tests/target/issue-3554.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_generics)]

pub struct S<const N: usize>;
impl S<{ 0 }> {}


