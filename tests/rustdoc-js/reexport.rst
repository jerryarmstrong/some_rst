tests/rustdoc-js/reexport.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test enforces that the (renamed) reexports are present in the search results.

pub mod fmt {
    pub struct Subscriber;
}
mod foo {
    pub struct AnotherOne;
}

pub use foo::AnotherOne;
pub use fmt::Subscriber as FmtSubscriber;


