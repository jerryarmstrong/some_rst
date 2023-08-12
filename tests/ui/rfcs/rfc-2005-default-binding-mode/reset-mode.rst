tests/ui/rfcs/rfc-2005-default-binding-mode/reset-mode.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we "reset" the mode as we pass through a `&` pattern.
//
// cc #46688

fn surprise(x: i32) {
    assert_eq!(x, 2);
}

fn main() {
    let x = &(1, &2);
    let (_, &b) = x;
    surprise(b);
}


