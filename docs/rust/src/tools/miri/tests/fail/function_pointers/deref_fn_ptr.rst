src/tools/miri/tests/fail/function_pointers/deref_fn_ptr.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() {}

fn main() {
    let x: u8 = unsafe {
        *std::mem::transmute::<fn(), *const u8>(f) //~ ERROR: out-of-bounds
    };
    panic!("this should never print: {}", x);
}


