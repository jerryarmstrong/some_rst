tests/ui/consts/auxiliary/external_macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(allow_internal_unstable)]

// Macro to help ensure CONST_ERR lint errors
// are not silenced in external macros.
// https://github.com/rust-lang/rust/issues/65300

#[macro_export]
#[allow_internal_unstable(type_ascription)]
macro_rules! static_assert {
    ($test:expr) => {
        #[allow(dead_code)]
        const _: () = [()][!($test: bool) as usize];
    }
}


