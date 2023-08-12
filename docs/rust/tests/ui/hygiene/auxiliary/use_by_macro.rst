tests/ui/hygiene/auxiliary/use_by_macro.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

macro x($macro_name:ident) {
    #[macro_export]
    macro_rules! $macro_name {
        (define) => {
            pub struct MyStruct;
        };
        (create) => {
            MyStruct {}
        };
    }
}

x!(my_struct);


