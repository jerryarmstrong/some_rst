src/tools/rustfmt/tests/source/issue-4791/trailing_comma.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-struct_field_align_threshold: 30
// rustfmt-trailing_comma: Always

struct Foo {
    group_a: u8,

    group_b: u8
}

struct Bar {
    group_a: u8,

    group_b: u8,
}


