tests/rustdoc/empty-impl-block.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has 'foo/struct.Foo.html'
pub struct Foo;

// @has - '//*[@class="docblock"]' 'Hello empty impl block!'
// @has - '//*[@class="item-info"]' 'This impl block contains no items.'
/// Hello empty impl block!
impl Foo {}
// We ensure that this empty impl block without doc isn't rendered.
// @count - '//*[@class="impl has-srclink"]' 'impl Foo' 1
impl Foo {}

// Just to ensure that empty trait impl blocks are rendered.
pub struct Another;
pub trait Bar {}

// @has 'foo/struct.Another.html'
// @has - '//h3[@class="code-header"]' 'impl Bar for Another'
impl Bar for Another {}


