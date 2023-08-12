tests/rustdoc/intra-doc/email-address.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![forbid(rustdoc::broken_intra_doc_links)]

//! Email me at <hello@example.com>.
//! Email me at <hello-world@example.com>.
//! Email me at <hello@localhost>.
//! Email me at <prim@i32>.
// @has email_address/index.html '//a[@href="mailto:hello@example.com"]' 'hello@example.com'
// @has email_address/index.html '//a[@href="mailto:hello-world@example.com"]' 'hello-world@example.com'
// @has email_address/index.html '//a[@href="mailto:hello@localhost"]' 'hello@localhost'
// @has email_address/index.html '//a[@href="mailto:prim@i32"]' 'prim@i32'


