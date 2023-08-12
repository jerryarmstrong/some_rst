tests/ui/hygiene/auxiliary/local_inner_macros.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! helper1 {
    () => ( struct S; )
}

#[macro_export(local_inner_macros)]
macro_rules! helper2 {
    () => ( helper1!(); )
}

#[macro_export(local_inner_macros)]
macro_rules! public_macro {
    () => ( helper2!(); )
}

#[macro_export(local_inner_macros)]
macro_rules! public_macro_dynamic {
    ($helper: ident) => ( $helper!(); )
}


