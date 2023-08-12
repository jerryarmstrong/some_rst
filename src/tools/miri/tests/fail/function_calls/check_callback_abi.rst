src/tools/miri/tests/fail/function_calls/check_callback_abi.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

extern "C" fn try_fn(_: *mut u8) {
    unreachable!();
}

fn main() {
    unsafe {
        // Make sure we check the ABI when Miri itself invokes a function
        // as part of a shim implementation.
        std::intrinsics::r#try(
            //~^ ERROR: calling a function with ABI C using caller ABI Rust
            std::mem::transmute::<extern "C" fn(*mut u8), _>(try_fn),
            std::ptr::null_mut(),
            |_, _| unreachable!(),
        );
    }
}


