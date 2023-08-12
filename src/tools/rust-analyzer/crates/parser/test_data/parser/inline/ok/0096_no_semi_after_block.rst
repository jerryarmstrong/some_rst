src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0096_no_semi_after_block.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    if true {}
    loop {}
    match () {}
    while true {}
    for _ in () {}
    {}
    {}
    macro_rules! test {
         () => {}
    }
    test!{}
}


