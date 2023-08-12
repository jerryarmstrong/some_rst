src/tools/clippy/tests/ui/double_comparison.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let x = 1;
    let y = 2;
    if x == y || x < y {
        // do something
    }
    if x < y || x == y {
        // do something
    }
    if x == y || x > y {
        // do something
    }
    if x > y || x == y {
        // do something
    }
    if x < y || x > y {
        // do something
    }
    if x > y || x < y {
        // do something
    }
    if x <= y && x >= y {
        // do something
    }
    if x >= y && x <= y {
        // do something
    }
}


