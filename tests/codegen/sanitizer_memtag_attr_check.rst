tests/codegen/sanitizer_memtag_attr_check.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This tests that the sanitize_memtag attribute is
// applied when enabling the memtag sanitizer.
//
// needs-sanitizer-memtag
// compile-flags: -Zsanitizer=memtag -Ctarget-feature=+mte

#![crate_type = "lib"]

// CHECK: ; Function Attrs:{{.*}}sanitize_memtag
pub fn tagged() {}

// CHECK: attributes #0 = {{.*}}sanitize_memtag


