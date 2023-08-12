tests/ui/drop/drop-with-type-ascription-1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let foo = "hello".to_string();
    let foo: Vec<&str> = foo.split_whitespace().collect();
    let invalid_string = &foo[0];
    assert_eq!(*invalid_string, "hello");
}


