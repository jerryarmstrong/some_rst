tests/rustdoc/intra-doc/extern-reference-link.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --extern pub_struct
// aux-build:pub-struct.rs

/// [SomeStruct]
///
/// [SomeStruct]: pub_struct::SomeStruct
pub fn foo() {}


