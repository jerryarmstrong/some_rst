tests/rustdoc/const-generics/const-generic-defaults.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/struct.Foo.html '//div[@class="item-decl"]/pre[@class="rust"]' \
//      'pub struct Foo<const M: usize = 10, const N: usize = M, T = i32>(_);'
pub struct Foo<const M: usize = 10, const N: usize = M, T = i32>(T);


