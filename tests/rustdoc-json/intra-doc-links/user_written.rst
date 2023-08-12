tests/rustdoc-json/intra-doc-links/user_written.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! For motivation, see [the reasons](foo#reasons)

/// # Reasons
/// To test rustdoc json
pub fn foo() {}

// @set foo = "$.index[*][?(@.name=='foo')].id"
// @is "$.index[*][?(@.name=='user_written')].links['foo#reasons']" $foo


