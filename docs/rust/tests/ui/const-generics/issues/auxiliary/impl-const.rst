tests/ui/const-generics/issues/auxiliary/impl-const.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]

pub struct Num<const N: usize>;

// Braces around const expression causes crash
impl Num<{5}> {
    pub fn five(&self) {
    }
}


