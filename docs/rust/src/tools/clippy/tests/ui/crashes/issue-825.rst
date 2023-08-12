src/tools/clippy/tests/ui/crashes/issue-825.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

/// Test for https://github.com/rust-lang/rust-clippy/issues/825

// this should compile in a reasonable amount of time
fn rust_type_id(name: &str) {
    if "bool" == &name[..]
        || "uint" == &name[..]
        || "u8" == &name[..]
        || "u16" == &name[..]
        || "u32" == &name[..]
        || "f32" == &name[..]
        || "f64" == &name[..]
        || "i8" == &name[..]
        || "i16" == &name[..]
        || "i32" == &name[..]
        || "i64" == &name[..]
        || "Self" == &name[..]
        || "str" == &name[..]
    {
        unreachable!();
    }
}

fn main() {}


