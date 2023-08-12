tests/codegen/non-terminate/infinite-loop-1.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C opt-level=3

#![crate_type = "lib"]

fn infinite_loop() -> u8 {
    loop {}
}

// CHECK-LABEL: @test
#[no_mangle]
fn test() -> u8 {
    // CHECK-NOT: unreachable
    // CHECK: br label %{{.+}}
    // CHECK-NOT: unreachable
    let x = infinite_loop();
    x
}


