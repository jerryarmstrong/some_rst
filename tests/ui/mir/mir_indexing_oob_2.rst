tests/ui/mir/mir_indexing_oob_2.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:index out of bounds: the len is 5 but the index is 10
// ignore-emscripten no processes

const C: &'static [u8; 5] = b"hello";

#[allow(unconditional_panic)]
fn test() -> u8 {
    C[10]
}

fn main() {
    test();
}


