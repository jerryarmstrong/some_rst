tests/rustdoc/sidebar-all-page.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

#![feature(rustdoc_internals)]

// @has 'foo/all.html'
// @has - '//*[@class="sidebar-elems"]//li' 'Structs'
// @has - '//*[@class="sidebar-elems"]//li' 'Enums'
// @has - '//*[@class="sidebar-elems"]//li' 'Unions'
// @has - '//*[@class="sidebar-elems"]//li' 'Functions'
// @has - '//*[@class="sidebar-elems"]//li' 'Traits'
// @has - '//*[@class="sidebar-elems"]//li' 'Macros'
// @has - '//*[@class="sidebar-elems"]//li' 'Type Definitions'
// @has - '//*[@class="sidebar-elems"]//li' 'Constants'
// @has - '//*[@class="sidebar-elems"]//li' 'Statics'
// @has - '//*[@class="sidebar-elems"]//li' 'Primitive Types'

pub struct Foo;
pub enum Enum {
    A,
}
pub union Bar {
    a: u8,
    b: u16,
}
pub fn foo() {}
pub trait Trait {}
#[macro_export]
macro_rules! foo {
    () => {}
}
pub type Type = u8;
pub const FOO: u8 = 0;
pub static BAR: u8 = 0;
#[doc(primitive = "u8")]
mod u8 {}


