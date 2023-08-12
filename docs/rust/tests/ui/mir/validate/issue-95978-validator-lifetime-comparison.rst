tests/ui/mir/validate/issue-95978-validator-lifetime-comparison.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Zvalidate-mir

fn foo(_a: &str) {}

fn main() {
    let x = foo as fn(&'static str);

    let _ = x == foo;
}


