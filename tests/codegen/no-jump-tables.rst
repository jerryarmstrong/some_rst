tests/codegen/no-jump-tables.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the `no-jump-tables` function attribute are (not) emitted when
// the `-Zno-jump-tables` flag is (not) set.

// revisions: unset set
// needs-llvm-components: x86
// compile-flags: --target x86_64-unknown-linux-gnu
// [set] compile-flags: -Zno-jump-tables

#![crate_type = "lib"]
#![feature(no_core, lang_items)]
#![no_core]

#[lang = "sized"]
trait Sized {}

#[no_mangle]
pub fn foo() {
    // CHECK: @foo() unnamed_addr #0

    // unset-NOT: attributes #0 = { {{.*}}"no-jump-tables"="true"{{.*}} }
    // set: attributes #0 = { {{.*}}"no-jump-tables"="true"{{.*}} }
}


