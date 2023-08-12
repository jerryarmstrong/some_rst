tests/rustdoc/foreigntype.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern "C" {
    // @has foreigntype/foreigntype.ExtType.html
    pub type ExtType;
}

impl ExtType {
    // @has - '//a[@class="fn"]' 'do_something'
    pub fn do_something(&self) {}
}

pub trait Trait {}

// @has foreigntype/trait.Trait.html '//a[@class="foreigntype"]' 'ExtType'
impl Trait for ExtType {}

// @has foreigntype/index.html '//a[@class="foreigntype"]' 'ExtType'


