tests/ui/test-attrs/test-runner-hides-start.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --test

#![feature(start)]

#[start]
fn start(_: isize, _: *const *const u8) -> isize { panic!(); }


