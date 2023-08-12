tests/ui/attr-start.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![feature(start)]

#[start]
fn start(_argc: isize, _argv: *const *const u8) -> isize {
    return 0;
}


