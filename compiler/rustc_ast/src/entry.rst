compiler/rustc_ast/src/entry.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Debug)]
pub enum EntryPointType {
    None,
    MainNamed,
    RustcMainAttr,
    Start,
    OtherMain, // Not an entry point, but some other function named main
}


