tests/ui/consts/const-match-pattern-arm.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const _: bool = match Some(true) {
    Some(value) => true,
    _ => false
};

const _: bool = {
    match Some(true) {
        Some(value) => true,
        _ => false
    }
};

fn main() {}


