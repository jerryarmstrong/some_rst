tests/ui/pattern/usefulness/issue-82772-match-box-as-struct.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This used to ICE in exhaustiveness checking. Explanation here:
// https://github.com/rust-lang/rust/issues/82772#issuecomment-905946768
fn main() {
    let Box { 1: _, .. }: Box<()>; //~ ERROR field `1` of
    let Box { .. }: Box<()>;
}


