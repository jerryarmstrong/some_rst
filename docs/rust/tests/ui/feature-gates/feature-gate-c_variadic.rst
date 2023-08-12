tests/ui/feature-gates/feature-gate-c_variadic.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

pub unsafe extern "C" fn test(_: i32, ap: ...) { }
//~^ C-variadic functions are unstable


