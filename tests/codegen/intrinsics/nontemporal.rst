tests/codegen/intrinsics/nontemporal.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

#![feature(core_intrinsics)]
#![crate_type = "lib"]

#[no_mangle]
pub fn a(a: &mut u32, b: u32) {
    // CHECK-LABEL: define{{.*}}void @a
    // CHECK: store i32 %b, {{i32\*|ptr}} %a, align 4, !nontemporal
    unsafe {
        std::intrinsics::nontemporal_store(a, b);
    }
}


