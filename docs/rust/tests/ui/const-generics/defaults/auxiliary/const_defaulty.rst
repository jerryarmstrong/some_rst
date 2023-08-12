tests/ui/const-generics/defaults/auxiliary/const_defaulty.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Defaulted<const N: usize=3>;
impl Defaulted {
    pub fn new() -> Self {
        Defaulted
    }
}
impl<const N: usize> Defaulted<N> {
    pub fn value(&self) -> usize {
        N
    }
}


