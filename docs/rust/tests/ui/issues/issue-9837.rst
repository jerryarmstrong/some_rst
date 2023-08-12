tests/ui/issues/issue-9837.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
const C1: i32 = 0x12345678;
const C2: isize = C1 as i16 as isize;

enum E {
    V = C2
}

fn main() {
    assert_eq!(C2 as u64, E::V as u64);
}


