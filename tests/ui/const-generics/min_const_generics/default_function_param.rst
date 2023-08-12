tests/ui/const-generics/min_const_generics/default_function_param.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

fn foo<const SIZE: usize = 5usize>() {}
//~^ ERROR defaults for const parameters are


