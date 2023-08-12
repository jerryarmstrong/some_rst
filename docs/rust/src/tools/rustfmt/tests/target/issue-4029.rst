src/tools/rustfmt/tests/target/issue-4029.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #4029
#[derive(Debug, Clone, Default Hash)]
struct S;

// issue #3898
#[derive(Debug, Clone, Default,, Hash)]
struct T;


