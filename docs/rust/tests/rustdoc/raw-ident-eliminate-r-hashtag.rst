tests/rustdoc/raw-ident-eliminate-r-hashtag.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

pub mod internal {
    // @has 'raw_ident_eliminate_r_hashtag/internal/struct.mod.html'
    #[allow(non_camel_case_types)]
    pub struct r#mod;

    /// See [name], [other name]
    ///
    /// [name]: mod
    /// [other name]: crate::internal::mod
    // @has 'raw_ident_eliminate_r_hashtag/internal/struct.B.html' '//*a[@href="struct.mod.html"]' 'name'
    // @has 'raw_ident_eliminate_r_hashtag/internal/struct.B.html' '//*a[@href="struct.mod.html"]' 'other name'
    pub struct B;
}

/// See [name].
///
/// [name]: internal::mod
// @has 'raw_ident_eliminate_r_hashtag/struct.A.html' '//*a[@href="internal/struct.mod.html"]' 'name'
pub struct A;


