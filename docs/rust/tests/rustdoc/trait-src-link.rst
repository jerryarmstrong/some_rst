tests/rustdoc/trait-src-link.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "quix"]
pub trait Foo {
    // @has quix/trait.Foo.html '//a[@href="../src/quix/trait-src-link.rs.html#4"]' 'source'
    fn required();

    // @has quix/trait.Foo.html '//a[@href="../src/quix/trait-src-link.rs.html#7"]' 'source'
    fn provided() {}
}

pub struct Bar;

impl Foo for Bar {
    // @has quix/struct.Bar.html '//a[@href="../src/quix/trait-src-link.rs.html#14"]' 'source'
    fn required() {}
    // @has quix/struct.Bar.html '//a[@href="../src/quix/trait-src-link.rs.html#7"]' 'source'
}

pub struct Baz;

impl Foo for Baz {
    // @has quix/struct.Baz.html '//a[@href="../src/quix/trait-src-link.rs.html#22"]' 'source'
    fn required() {}

    // @has quix/struct.Baz.html '//a[@href="../src/quix/trait-src-link.rs.html#25"]' 'source'
    fn provided() {}
}


