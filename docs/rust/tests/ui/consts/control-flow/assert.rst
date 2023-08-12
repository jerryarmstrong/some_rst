tests/ui/consts/control-flow/assert.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `assert` works in consts.

const _: () = assert!(true);

const _: () = assert!(false);
//~^ ERROR evaluation of constant value failed

fn main() {}


