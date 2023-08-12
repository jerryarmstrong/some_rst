tests/ui/parser/new-unicode-escapes-2.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let s = "\u{260311111111}"; //~ ERROR overlong unicode escape
}


