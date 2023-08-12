tests/ui/consts/const-for-feature-gate.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-const_for

const _: () = {
    for _ in 0..5 {}
    //~^ error: `for` is not allowed in a `const`
};

fn main() {}


