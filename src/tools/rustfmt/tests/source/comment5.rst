src/tools/rustfmt/tests/source/comment5.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
// rustfmt-wrap_comments: true

//@ special comment
//@ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec adiam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam
//@
//@foo
fn test() {}

//@@@ another special comment
//@@@ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec adiam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam
//@@@
//@@@foo
fn bar() {}


