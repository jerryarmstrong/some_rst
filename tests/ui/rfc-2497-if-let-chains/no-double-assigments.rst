tests/ui/rfc-2497-if-let-chains/no-double-assigments.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    loop {
        // [1][0] should leave top scope
        if true && [1][0] == 1 && true {
        }
    }
}


