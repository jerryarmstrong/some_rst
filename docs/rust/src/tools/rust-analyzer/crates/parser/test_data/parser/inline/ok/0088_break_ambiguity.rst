src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0088_break_ambiguity.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(){
    if break {}
    while break {}
    for i in break {}
    match break {}
}


