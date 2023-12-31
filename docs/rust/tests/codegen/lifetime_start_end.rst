tests/codegen/lifetime_start_end.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O -C no-prepopulate-passes -Zmir-opt-level=0

#![crate_type = "lib"]

// CHECK-LABEL: @test
#[no_mangle]
pub fn test() {
    let a = 0u8;
    &a; // keep variable in an alloca

// CHECK: call void @llvm.lifetime.start{{.*}}(i{{[0-9 ]+}}, {{i8\*|ptr}} %a)

    {
        let b = &Some(a);
        &b; // keep variable in an alloca

// CHECK: call void @llvm.lifetime.start{{.*}}(i{{[0-9 ]+}}, {{.*}})

// CHECK: call void @llvm.lifetime.start{{.*}}(i{{[0-9 ]+}}, {{.*}})

// CHECK: call void @llvm.lifetime.end{{.*}}(i{{[0-9 ]+}}, {{.*}})

// CHECK: call void @llvm.lifetime.end{{.*}}(i{{[0-9 ]+}}, {{.*}})
    }

    let c = 1u8;
    &c; // keep variable in an alloca

// CHECK: call void @llvm.lifetime.start{{.*}}(i{{[0-9 ]+}}, {{i8\*|ptr}} %c)

// CHECK: call void @llvm.lifetime.end{{.*}}(i{{[0-9 ]+}}, {{i8\*|ptr}} %c)

// CHECK: call void @llvm.lifetime.end{{.*}}(i{{[0-9 ]+}}, {{i8\*|ptr}} %a)
}


