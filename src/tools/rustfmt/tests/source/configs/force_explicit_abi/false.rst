src/tools/rustfmt/tests/source/configs/force_explicit_abi/false.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-force_explicit_abi: false
// Force explicit abi

extern {
    pub static lorem: c_int;
}


