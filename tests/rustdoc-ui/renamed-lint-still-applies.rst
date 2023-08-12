tests/rustdoc-ui/renamed-lint-still-applies.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-args: --crate-type lib
#![deny(broken_intra_doc_links)]
//~^ WARNING renamed to `rustdoc::broken_intra_doc_links`
//! [x]
//~^ ERROR unresolved link

#![deny(rustdoc::non_autolinks)]
//~^ WARNING renamed to `rustdoc::bare_urls`
//! http://example.com
//~^ ERROR not a hyperlink


