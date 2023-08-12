src/tools/rustfmt/tests/target/issue-4984/multi_line_derive.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(
    /* ---------- Some really important comment that just had to go inside the derive --------- */
    Debug,
    Clone,
    Eq,
    PartialEq,
)]
struct Foo {
    a: i32,
    b: T,
}

#[derive(
    /*
        Some really important comment that just had to go inside the derive.
        Also had to be put over multiple lines
    */
    Debug,
    Clone,
    Eq,
    PartialEq,
)]
struct Bar {
    a: i32,
    b: T,
}


