tests/ui/issues/issue-6130.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: usize = 0;
    assert!(i <= 0xFFFF_FFFF);

    let i: isize = 0;
    assert!(i >= -0x8000_0000);
    assert!(i <= 0x7FFF_FFFF);
}


