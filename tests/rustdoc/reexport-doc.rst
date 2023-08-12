tests/rustdoc/reexport-doc.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:reexport-doc-aux.rs

extern crate reexport_doc_aux as dep;

// @has 'reexport_doc/struct.Foo.html'
// @count - '//p' 'These are the docs for Foo.' 1
/// These are the docs for Foo.
pub use dep::Foo;


