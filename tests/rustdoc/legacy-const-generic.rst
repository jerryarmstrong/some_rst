tests/rustdoc/legacy-const-generic.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]
#![feature(rustc_attrs)]

// @has 'foo/fn.foo.html'
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'fn foo(x: usize, const Y: usize, z: usize) -> [usize; 3]'
#[rustc_legacy_const_generics(1)]
pub fn foo<const Y: usize>(x: usize, z: usize) -> [usize; 3] {
    [x, Y, z]
}

// @has 'foo/fn.bar.html'
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'fn bar(x: usize, const Y: usize, const Z: usize) -> [usize; 3]'
#[rustc_legacy_const_generics(1, 2)]
pub fn bar<const Y: usize, const Z: usize>(x: usize) -> [usize; 3] {
    [x, Y, z]
}


