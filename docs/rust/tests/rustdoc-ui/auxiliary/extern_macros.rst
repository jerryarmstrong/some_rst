tests/rustdoc-ui/auxiliary/extern_macros.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! attrs_on_struct {
    ( $( #[$attr:meta] )* ) => {
        $( #[$attr] )*
        pub struct ExpandedStruct;
    }
}


