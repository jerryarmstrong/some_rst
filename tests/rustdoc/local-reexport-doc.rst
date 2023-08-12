tests/rustdoc/local-reexport-doc.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test ensures that the reexports of local items also get the doc from
// the reexport.

#![crate_name = "foo"]

// @has 'foo/fn.g.html'
// @has - '//*[@class="toggle top-doc"]/*[@class="docblock"]' \
// 'outer module inner module'

mod inner_mod {
    /// inner module
    pub fn g() {}
}

/// outer module
pub use inner_mod::g;


