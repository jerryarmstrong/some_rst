tests/run-make/issue-85401-static-mir/bar.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn bar() {
    println!("bar {}", foo::FOO);
    foo::foo();
}


