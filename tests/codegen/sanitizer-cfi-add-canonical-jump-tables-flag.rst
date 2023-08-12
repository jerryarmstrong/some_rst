tests/codegen/sanitizer-cfi-add-canonical-jump-tables-flag.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verifies that "CFI Canonical Jump Tables" module flag is added.
//
// needs-sanitizer-cfi
// compile-flags: -Clto -Ctarget-feature=-crt-static -Zsanitizer=cfi

#![crate_type="lib"]

pub fn foo() {
}

// CHECK: !{{[0-9]+}} = !{i32 2, !"CFI Canonical Jump Tables", i32 1}


