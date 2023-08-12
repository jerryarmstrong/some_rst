tests/ui/feature-gates/feature-gate-try_blocks.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018

pub fn main() {
    let try_result: Option<_> = try { //~ ERROR `try` expression is experimental
        let x = 5;
        x
    };
    assert_eq!(try_result, Some(5));
}


