tests/codegen/move-operands.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C no-prepopulate-passes -Zmir-enable-passes=+DestinationPropagation

#![crate_type = "lib"]

type T = [u8; 256];

#[no_mangle]
pub fn f(a: T, b: fn(_: T, _: T)) {
    // CHECK: call void @llvm.memcpy.{{.*}}({{i8\*|ptr}} align 1 %{{.*}}, {{i8\*|ptr}} align 1 %{{.*}}, {{.*}} 256, i1 false)
    // CHECK-NOT: call void @llvm.memcpy.{{.*}}({{i8\*|ptr}} align 1 %{{.*}}, {{i8\*|ptr}} align 1 %{{.*}}, {{.*}} 256, i1 false)
    b(a, a)
}


