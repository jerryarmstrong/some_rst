tests/ui-fulldeps/pathless-extern-unstable.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-stage1
// edition:2018
// compile-flags:--extern rustc_middle

// Test that `--extern rustc_middle` fails with `rustc_private`.

pub use rustc_middle;
//~^ ERROR use of unstable library feature 'rustc_private'

fn main() {}


