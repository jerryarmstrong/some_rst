tests/ui/parser/issue-99910-const-let-mutually-exclusive.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    const let _FOO: i32 = 123;
    //~^ ERROR const` and `let` are mutually exclusive
    let const _BAR: i32 = 123;
    //~^ ERROR `const` and `let` are mutually exclusive
}


