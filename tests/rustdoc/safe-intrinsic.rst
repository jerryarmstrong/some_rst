tests/rustdoc/safe-intrinsic.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]
#![feature(no_core)]
#![feature(rustc_attrs)]

#![no_core]
#![crate_name = "foo"]

extern "rust-intrinsic" {
    // @has 'foo/fn.abort.html'
    // @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub extern "rust-intrinsic" fn abort() -> !'
    #[rustc_safe_intrinsic]
    pub fn abort() -> !;
    // @has 'foo/fn.unreachable.html'
    // @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub unsafe extern "rust-intrinsic" fn unreachable() -> !'
    pub fn unreachable() -> !;
}

extern "C" {
    // @has 'foo/fn.needs_drop.html'
    // @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub unsafe extern "C" fn needs_drop() -> !'
    pub fn needs_drop() -> !;
}


