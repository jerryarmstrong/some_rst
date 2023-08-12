tests/ui/expr/if/issue-4201.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = if true {
        0
    } else if false {
//~^ ERROR `if` may be missing an `else` clause
//~| expected integer, found `()`
        1
    };
}


