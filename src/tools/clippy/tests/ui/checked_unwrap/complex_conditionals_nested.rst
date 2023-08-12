src/tools/clippy/tests/ui/checked_unwrap/complex_conditionals_nested.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::panicking_unwrap, clippy::unnecessary_unwrap)]
#![allow(clippy::if_same_then_else, clippy::branches_sharing_code)]

fn test_nested() {
    fn nested() {
        let x = Some(());
        if x.is_some() {
            x.unwrap(); // unnecessary
        } else {
            x.unwrap(); // will panic
        }
    }
}

fn main() {}


