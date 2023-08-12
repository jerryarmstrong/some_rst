tests/ui/hygiene/auxiliary/codegen-attrs.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

macro m($f:ident) {
    #[export_name = "export_function_name"]
    pub fn $f() -> i32 {
        2
    }
}

m!(rust_function_name);


