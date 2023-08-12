tests/ui/imports/auxiliary/import_crate_var.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn f() {}

#[macro_export]
macro_rules! m { () => {
    use $crate;
    import_crate_var::f();
} }


