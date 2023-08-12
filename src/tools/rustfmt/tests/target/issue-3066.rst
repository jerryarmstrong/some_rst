src/tools/rustfmt/tests/target/issue-3066.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
fn main() {
    Struct { field: aaaaaaaaaaa };
    Struct { field: aaaaaaaaaaaa };
    Struct { field: value,
             field2: value2 };
}


