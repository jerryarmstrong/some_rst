tests/rustdoc/remove-duplicates.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

mod foo {
    pub use bar::*;
    pub mod bar {
        pub trait Foo {
            fn foo();
        }
    }
}

// @count foo/index.html '//*[@class="trait"]' 1
pub use foo::bar::*;
pub use foo::*;


