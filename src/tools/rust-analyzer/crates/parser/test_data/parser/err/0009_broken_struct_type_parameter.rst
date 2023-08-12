src/tools/rust-analyzer/crates/parser/test_data/parser/err/0009_broken_struct_type_parameter.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<90 + 2> {
    f: u32
}

struct T;


