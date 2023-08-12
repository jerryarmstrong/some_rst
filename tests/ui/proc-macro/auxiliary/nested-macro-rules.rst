tests/ui/proc-macro/auxiliary/nested-macro-rules.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct FirstStruct;

#[macro_export]
macro_rules! outer_macro {
    ($name:ident, $attr_struct_name:ident) => {
        #[macro_export]
        macro_rules! inner_macro {
            ($bang_macro:ident, $attr_macro:ident) => {
                $bang_macro!($name);
                #[$attr_macro] struct $attr_struct_name {}
            }
        }
    }
}

outer_macro!(FirstStruct, FirstAttrStruct);


