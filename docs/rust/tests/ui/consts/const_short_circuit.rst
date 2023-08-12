tests/ui/consts/const_short_circuit.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const _: bool = false && false;
const _: bool = true && false;
const _: bool = {
    let mut x = true && false;
    x
};
const _: bool = {
    let x = true && false;
    x
};

fn main() {}


