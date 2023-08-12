src/tools/miri/tests/fail/intrinsics/assume.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

fn main() {
    let x = 5;
    unsafe {
        std::intrinsics::assume(x < 10);
        std::intrinsics::assume(x > 1);
        std::intrinsics::assume(x > 42); //~ ERROR: `assume` called with `false`
    }
}


