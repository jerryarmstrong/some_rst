src/tools/rustfmt/tests/source/match-flattening.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match option {
        None => if condition {
            true
        } else {
            false
        },
    }
}

fn main() {
    match option {
        None => {
            if condition {
                true
            } else {
                false
            }
        }
    }
}


