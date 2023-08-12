tests/run-make/issue-85401-static-mir/foo.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub static FOO: &str = "foo";

pub fn foo() {
    println!("foo");
}


