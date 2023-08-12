src/tools/rustfmt/tests/target/issue-4926/minimum_example.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-struct_field_align_threshold: 30

struct X {
    a: i32,
    b: i32,
}

fn test(x: X) {
    let y = matches!(x, X { a: 1, .. });
}


