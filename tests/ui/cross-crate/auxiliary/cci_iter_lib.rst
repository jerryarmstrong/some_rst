tests/ui/cross-crate/auxiliary/cci_iter_lib.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="cci_iter_lib"]

#[inline]
pub fn iter<T, F>(v: &[T], mut f: F) where F: FnMut(&T) {
    let mut i = 0;
    let n = v.len();
    while i < n {
        f(&v[i]);
        i += 1;
    }
}


