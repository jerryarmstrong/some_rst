tests/rustdoc/pub-use-extern-macros.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:pub-use-extern-macros.rs

extern crate macros;

// @has pub_use_extern_macros/macro.bar.html
// @!has pub_use_extern_macros/index.html '//code' 'pub use macros::bar;'
pub use macros::bar;

// @has pub_use_extern_macros/macro.baz.html
// @!has pub_use_extern_macros/index.html '//code' 'pub use macros::baz;'
#[doc(inline)]
pub use macros::baz;

// @!has pub_use_extern_macros/macro.quux.html
// @!has pub_use_extern_macros/index.html '//code' 'pub use macros::quux;'
#[doc(hidden)]
pub use macros::quux;


