tests/ui/methods/auxiliary/ambig_impl_2_lib.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Me {
    fn me(&self) -> usize;
}
impl Me for usize { fn me(&self) -> usize { *self } }


