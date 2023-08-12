src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0016_struct_flavors.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A;
struct B {}
struct C();

struct D {
    a: u32,
    pub b: u32
}

struct E(pub x, y,);


