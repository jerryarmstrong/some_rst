tests/ui/hygiene/cross-crate-variants.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that variants of an enum defined in another crate are resolved
// correctly when their names differ only in `SyntaxContext`.

// run-pass
// aux-build:variants.rs

extern crate variants;

use variants::*;

fn main() {
    check_variants();

    test_variants!();
    test_variants2!();

    assert_eq!(MyEnum::Variant as u8, 1);
}


