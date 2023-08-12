src/tools/miri/tests/fail/validity/cast_fn_ptr1.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-permissive-provenance

fn main() {
    // Cast a function pointer such that on a call, the argument gets transmuted
    // from raw ptr to reference. This is ABI-compatible, so it's not the call that
    // should fail, but validation should.
    fn f(_x: &i32) {}

    let g: fn(*const i32) = unsafe { std::mem::transmute(f as fn(&i32)) };

    g(0usize as *const i32)
    //~^ ERROR: encountered a null reference
}


