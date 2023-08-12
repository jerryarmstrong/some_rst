tests/ui/consts/const-eval/unused-broken-const.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // make sure that an *unused* broken const triggers an error even in a check build

// compile-flags: --emit=dep-info,metadata

const FOO: i32 = [][0];
//~^ ERROR evaluation of constant value failed

fn main() {}


