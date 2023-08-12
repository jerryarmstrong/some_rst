src/tools/rustfmt/tests/target/attrib-extern-crate.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Attributes on extern crate.

#[Attr1]
extern crate Bar;
#[Attr2]
#[Attr2]
extern crate Baz;
extern crate Foo;

fn foo() {
    #[Attr1]
    extern crate Bar;
    #[Attr2]
    #[Attr2]
    extern crate Baz;
    extern crate Foo;
}


