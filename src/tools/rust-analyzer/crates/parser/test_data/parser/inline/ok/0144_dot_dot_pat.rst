src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0144_dot_dot_pat.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let .. = ();
    //
    // Tuples
    //
    let (a, ..) = ();
    let (a, ..,) = ();
    let Tuple(a, ..) = ();
    let Tuple(a, ..,) = ();
    let (.., ..) = ();
    let Tuple(.., ..) = ();
    let (.., a, ..) = ();
    let Tuple(.., a, ..) = ();
    //
    // Slices
    //
    let [..] = ();
    let [head, ..] = ();
    let [head, tail @ ..] = ();
    let [head, .., cons] = ();
    let [head, mid @ .., cons] = ();
    let [head, .., .., cons] = ();
    let [head, .., mid, tail @ ..] = ();
    let [head, .., mid, .., cons] = ();
}


