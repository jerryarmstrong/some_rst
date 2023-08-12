tests/codegen/dealloc-no-unwind.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-system-llvm
// compile-flags: -O

#![crate_type="lib"]

struct A;

impl Drop for A {
    fn drop(&mut self) {
        extern "C" { fn foo(); }
        unsafe { foo(); }
    }
}

#[no_mangle]
pub fn a(a: Box<i32>) {
    // CHECK-LABEL: define{{.*}}void @a
    // CHECK: call void @__rust_dealloc
    // CHECK-NEXT: call void @foo
    let _a = A;
    drop(a);
}


