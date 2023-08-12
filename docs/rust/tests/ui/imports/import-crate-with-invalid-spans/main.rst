tests/ui/imports/import-crate-with-invalid-spans/main.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:crate_with_invalid_spans.rs

// pretty-expanded FIXME #23616

extern crate crate_with_invalid_spans;

fn main() {
    // The AST of `exported_generic` stored in crate_with_invalid_spans's
    // metadata should contain an invalid span where span.lo() > span.hi().
    // Let's make sure the compiler doesn't crash when encountering this.
    let _ = crate_with_invalid_spans::exported_generic(32u32, 7u32);
}


