src/tools/rust-analyzer/crates/parser/test_data/parser/err/0048_double_fish.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() {
    S::<Item::<lol>::<nope>>;
}

fn g() {
    let _: Item::<lol>::<nope> = ();
}


