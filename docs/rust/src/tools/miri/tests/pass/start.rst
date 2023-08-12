src/tools/miri/tests/pass/start.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(start)]

#[start]
fn start(_: isize, _: *const *const u8) -> isize {
    println!("Hello from start!");

    0
}


