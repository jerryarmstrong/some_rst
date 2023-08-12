tests/ui/rfc-2497-if-let-chains/ast-pretty-check.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z unpretty=expanded

fn main() {
    if let 0 = 1 {}
}


