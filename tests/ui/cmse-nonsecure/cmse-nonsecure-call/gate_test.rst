tests/ui/cmse-nonsecure/cmse-nonsecure-call/gate_test.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-abi_c_cmse_nonsecure_call
fn main() {
    let non_secure_function = unsafe {
        core::mem::transmute::<usize, extern "C-cmse-nonsecure-call" fn(i32, i32, i32, i32) -> i32>(
        //~^ ERROR [E0658]
            0x10000004,
        )
    };
    let mut toto = 5;
    toto += non_secure_function(toto, 2, 3, 5);
}


