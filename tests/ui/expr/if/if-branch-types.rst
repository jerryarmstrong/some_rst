tests/ui/expr/if/if-branch-types.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = if true { 10i32 } else { 10u32 };
    //~^ ERROR `if` and `else` have incompatible types
    //~| expected `i32`, found `u32`
}


