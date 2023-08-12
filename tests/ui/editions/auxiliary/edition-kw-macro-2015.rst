tests/ui/editions/auxiliary/edition-kw-macro-2015.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2015

#![allow(keyword_idents)]

#[macro_export]
macro_rules! produces_async {
    () => (pub fn async() {})
}

#[macro_export]
macro_rules! produces_async_raw {
    () => (pub fn r#async() {})
}

#[macro_export]
macro_rules! consumes_async {
    (async) => (1)
}

#[macro_export]
macro_rules! consumes_async_raw {
    (r#async) => (1)
}

#[macro_export]
macro_rules! passes_ident {
    ($i: ident) => ($i)
}


