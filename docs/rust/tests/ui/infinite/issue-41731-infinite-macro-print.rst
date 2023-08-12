tests/ui/infinite/issue-41731-infinite-macro-print.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z trace-macros

#![recursion_limit = "5"]

fn main() {
    macro_rules! stack {
        ($overflow:expr) => {
            print!(stack!($overflow));
            //~^ ERROR recursion limit reached while expanding
            //~| ERROR format argument must be a string literal
        };
    }

    stack!("overflow");
}


