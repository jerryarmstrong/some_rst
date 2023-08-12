tests/ui/macros/macro-block-nonterminal.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

macro_rules! do_block{
    ($val:block) => {$val}
}

fn main() {
    let s;
    do_block!({ s = "it works!"; });
    assert_eq!(s, "it works!");
}


