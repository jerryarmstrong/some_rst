tests/ui/async-await/issue-66387-if-without-else.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
async fn f() -> i32 {
    if true { //~ ERROR `if` may be missing an `else` clause
        return 0;
    }
    // An `if` block without `else` causes the type table not to have a type for this expr.
    // Check that we do not unconditionally access the type table and we don't ICE.
}

fn main() {}


