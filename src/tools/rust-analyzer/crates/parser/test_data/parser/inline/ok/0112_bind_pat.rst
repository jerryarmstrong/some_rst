src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0112_bind_pat.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = ();
    let mut b = ();
    let ref c = ();
    let ref mut d = ();
    let e @ _ = ();
    let ref mut f @ g @ _ = ();
}


