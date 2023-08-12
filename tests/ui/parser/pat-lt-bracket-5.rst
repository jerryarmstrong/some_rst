tests/ui/parser/pat-lt-bracket-5.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v[0] = v[1]; //~ ERROR expected one of `:`, `;`, `=`, `@`, or `|`, found `[`
}


