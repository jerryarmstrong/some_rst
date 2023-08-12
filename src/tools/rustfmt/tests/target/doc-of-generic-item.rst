src/tools/rustfmt/tests/target/doc-of-generic-item.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Non-doc pre-comment of Foo
/// doc of Foo
// Non-doc post-comment of Foo
struct Foo<
    // Non-doc pre-comment of 'a
    /// doc of 'a
    'a,
    // Non-doc pre-comment of T
    /// doc of T
    T,
    // Non-doc pre-comment of N
    /// doc of N
    const N: item,
>;


