src/tools/rustfmt/tests/mod-resolver/issue-4874/main.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("Hello, world!");
}

mod foo;
mod bar {
    mod baz;
}

