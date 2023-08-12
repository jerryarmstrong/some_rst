tests/ui/parser/mismatched-delim-brace-empty-block.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {

}
    let _ = ();
} //~ ERROR unexpected closing delimiter


