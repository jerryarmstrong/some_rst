src/tools/miri/tests/fail/validity/invalid_bool.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _b = unsafe { std::mem::transmute::<u8, bool>(2) }; //~ ERROR: expected a boolean
}


