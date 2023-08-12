tests/ui/raw-ref-op/raw-ref-op.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(raw_ref_op)]

fn main() {
    let mut x = 123;
    let c_p = &raw const x;
    let m_p = &raw mut x;
    let i_r = &x;
    assert!(c_p == i_r);
    assert!(c_p == m_p);
    unsafe { assert!(*c_p == *i_r ); }
}


