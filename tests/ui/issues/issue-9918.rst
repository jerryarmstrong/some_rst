tests/ui/issues/issue-9918.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    assert_eq!((0 + 0u8) as char, '\0');
}


