tests/ui/expr/if/attrs/gate-whole-expr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let x = 1;

    #[cfg(FALSE)]
    if false {
        x = 2;
    } else if true {
        x = 3;
    } else {
        x = 4;
    }
    assert_eq!(x, 1);
}


