tests/rustdoc/sidebar-links-to-foreign-impl.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #56018: "Implementations on Foreign Types" sidebar items should link to specific impls

#![crate_name = "foo"]

// @has foo/trait.Foo.html
// @has - '//div[@class="sidebar-elems"]//h3/a[@href="#foreign-impls"]' 'Implementations on Foreign Types'
// @has - '//h2[@id="foreign-impls"]' 'Implementations on Foreign Types'
// @has - '//*[@class="sidebar-elems"]//section//a[@href="#impl-Foo-for-u32"]' 'u32'
// @has - '//*[@id="impl-Foo-for-u32"]//h3[@class="code-header"]' 'impl Foo for u32'
// @has - '//*[@class="sidebar-elems"]//section//a[@href="#impl-Foo-for-%26%27a%20str"]' "&'a str"
// @has - '//*[@id="impl-Foo-for-%26%27a%20str"]//h3[@class="code-header"]' "impl<'a> Foo for &'a str"
pub trait Foo {}

impl Foo for u32 {}

impl<'a> Foo for &'a str {}


