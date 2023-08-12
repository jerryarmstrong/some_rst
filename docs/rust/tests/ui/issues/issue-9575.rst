tests/ui/issues/issue-9575.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(start)]

#[start]
fn start(argc: isize, argv: *const *const u8, crate_map: *const u8) -> isize {
    //~^ `#[start]` function has wrong type
   0
}


