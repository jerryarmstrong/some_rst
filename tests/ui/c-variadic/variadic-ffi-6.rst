tests/ui/c-variadic/variadic-ffi-6.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]
#![feature(c_variadic)]

pub unsafe extern "C" fn use_vararg_lifetime(
    x: usize,
    y: ...
) -> &usize { //~ ERROR missing lifetime specifier
    &0
}

pub unsafe extern "C" fn use_normal_arg_lifetime(x: &usize, y: ...) -> &usize { // OK
    x
}


