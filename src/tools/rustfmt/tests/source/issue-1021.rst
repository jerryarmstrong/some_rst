src/tools/rustfmt/tests/source/issue-1021.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
fn main() {
    match x {
        S(true , .., true ) => (),
        S(true , .. ) => (),
        S(.., true ) => (),
        S( .. ) => (),
        S(_) => (),
        S(/* .. */ .. ) => (),
        S(/* .. */ .., true ) => (),
    }

    match y {
        (true , .., true ) => (),
        (true , .. ) => (),
        (.., true ) => (),
        ( .. ) => (),
        (_,) => (),
        (/* .. */ .. ) => (),
        (/* .. */ .., true ) => (),
    }
}


