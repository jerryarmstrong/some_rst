tests/ui/editions/auxiliary/edition-imports-2018.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#[macro_export]
macro_rules! gen_imports { () => {
    use import::Path;
    use std::collections::LinkedList;

    fn check_absolute() {
        ::absolute::Path;
        ::std::collections::LinkedList::<u8>::new();
    }
}}

#[macro_export]
macro_rules! gen_glob { () => {
    use *;
}}


