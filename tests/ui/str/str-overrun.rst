tests/ui/str/str-overrun.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:index out of bounds: the len is 5 but the index is 5
// ignore-emscripten no processes

fn main() {
    let s: String = "hello".to_string();

    // Bounds-check panic.
    assert_eq!(s.as_bytes()[5], 0x0 as u8);
}


