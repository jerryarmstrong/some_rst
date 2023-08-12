tests/ui/array-slice-vec/vec-macro-with-comma-only.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    vec![,]; //~ ERROR no rules expected the token `,`
}


