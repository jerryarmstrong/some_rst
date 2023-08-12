src/tools/miri/tests/pass/cast_fn_ptr.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f(_: *const u8) {}

    let g = unsafe { std::mem::transmute::<fn(*const u8), fn(*const i32)>(f) };

    g(&42 as *const _);
}


