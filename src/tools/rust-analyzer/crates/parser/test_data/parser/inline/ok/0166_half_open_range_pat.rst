src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0166_half_open_range_pat.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() {
    let 0 .. = 1u32;
    let 0..: _ = 1u32;

    match 42 {
        0 .. if true => (),
        _ => (),
    }
}


