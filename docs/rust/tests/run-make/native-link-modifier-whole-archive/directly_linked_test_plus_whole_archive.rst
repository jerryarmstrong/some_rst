tests/run-make/native-link-modifier-whole-archive/directly_linked_test_plus_whole_archive.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::io::Write;

#[test]
fn test_thing() {
    print!("ran the test");
    std::io::stdout().flush().unwrap();
}


