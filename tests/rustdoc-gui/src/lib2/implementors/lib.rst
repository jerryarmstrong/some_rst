tests/rustdoc-gui/src/lib2/implementors/lib.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Whatever {
    type Foo;

    fn method() {}
}

pub struct Struct;

impl Whatever for Struct {
    type Foo = u8;
}

impl http::HttpTrait for Struct {}

mod traits {
    pub trait TraitToReexport {
        fn method() {}
    }
}

#[doc(inline)]
pub use traits::TraitToReexport;


