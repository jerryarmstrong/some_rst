tests/ui/macros/macro-expanded-include/foo/mod.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test

macro_rules! m {
    () => { include!("file.txt"); }
}

macro_rules! n {
    () => { unsafe { core::arch::asm!(include_str!("file.txt")); } }
}


