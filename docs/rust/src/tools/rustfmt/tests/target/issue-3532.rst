src/tools/rustfmt/tests/target/issue-3532.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(a: T) {
    match a {
        1 => {}
        0 => {} // _ => panic!("doesn't format!"),
    }
}


