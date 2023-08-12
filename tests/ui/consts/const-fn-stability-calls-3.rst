tests/ui/consts/const-fn-stability-calls-3.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test use of const fn from another crate without a feature gate.

// check-pass
// aux-build:const_fn_lib.rs

extern crate const_fn_lib;

use const_fn_lib::foo;

fn main() {
    let x = foo(); // use outside a constant is ok
}


