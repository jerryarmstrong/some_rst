tests/ui/mir/mir_indexing_oob_1.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:index out of bounds: the len is 5 but the index is 10
// ignore-emscripten no processes

const C: [u32; 5] = [0; 5];

#[allow(unconditional_panic)]
fn test() -> u32 {
    C[10]
}

fn main() {
    test();
}


