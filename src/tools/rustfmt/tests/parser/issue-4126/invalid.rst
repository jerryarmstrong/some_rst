src/tools/rustfmt/tests/parser/issue-4126/invalid.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    if bar && if !baz {
        next_is_none = Some(true);
    }
    println!("foo");
}


