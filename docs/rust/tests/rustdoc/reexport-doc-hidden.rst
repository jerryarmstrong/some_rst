tests/rustdoc/reexport-doc-hidden.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Part of <https://github.com/rust-lang/rust/issues/59368>.
// This test ensures that reexporting a `doc(hidden)` item will
// still show the reexport.

#![crate_name = "foo"]

#[doc(hidden)]
pub type Type = u32;

// @has 'foo/index.html'
// @has - '//*[@id="reexport.Type2"]/code' 'pub use crate::Type as Type2;'
pub use crate::Type as Type2;

// @count - '//*[@id="reexport.Type3"]' 0
#[doc(hidden)]
pub use crate::Type as Type3;

#[macro_export]
#[doc(hidden)]
macro_rules! foo {
    () => {};
}

// This is a bug: https://github.com/rust-lang/rust/issues/59368
// @!has - '//*[@id="reexport.Macro"]/code' 'pub use crate::foo as Macro;'
pub use crate::foo as Macro;


