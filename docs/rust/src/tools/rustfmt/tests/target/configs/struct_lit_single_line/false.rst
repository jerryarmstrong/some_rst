src/tools/rustfmt/tests/target/configs/struct_lit_single_line/false.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-struct_lit_single_line: false
// Struct literal multiline-style

fn main() {
    let lorem = Lorem {
        ipsum: dolor,
        sit: amet,
    };
}


