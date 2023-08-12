src/tools/rustfmt/tests/target/issue-2781.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub // Oh, no. A line comment.
struct Foo {}

pub /* Oh, no. A block comment. */ struct Foo {}

mod inner {
    pub // Oh, no. A line comment.
    struct Foo {}

    pub /* Oh, no. A block comment. */ struct Foo {}
}


