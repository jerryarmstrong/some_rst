src/tools/rustfmt/tests/target/issue-4791/no_trailing_comma.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-struct_field_align_threshold: 0
// rustfmt-trailing_comma: Never

pub struct Baz {
    group_a: u8,

    group_b: u8
}


