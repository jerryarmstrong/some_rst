tests/ui/cross-crate/auxiliary/cci_impl_lib.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="cci_impl_lib"]

pub trait uint_helpers {
    fn to<F>(&self, v: usize, f: F) where F: FnMut(usize);
}

impl uint_helpers for usize {
    #[inline]
    fn to<F>(&self, v: usize, mut f: F) where F: FnMut(usize) {
        let mut i = *self;
        while i < v {
            f(i);
            i += 1;
        }
    }
}


