tests/codegen/sanitizer-kcfi-add-kcfi-flag.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verifies that "kcfi" module flag is added.
//
// needs-sanitizer-kcfi
// compile-flags: -Ctarget-feature=-crt-static -Zsanitizer=kcfi

#![crate_type="lib"]

pub fn foo() {
}

// CHECK: !{{[0-9]+}} = !{i32 4, !"kcfi", i32 1}


