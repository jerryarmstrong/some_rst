src/tools/rustfmt/tests/target/configs/force_explicit_abi/true.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-force_explicit_abi: true
// Force explicit abi

extern "C" {
    pub static lorem: c_int;
}


