tests/ui/parser/new-unicode-escapes-3.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let s1 = "\u{d805}"; //~ ERROR invalid unicode character escape
    let s2 = "\u{ffffff}"; //~ ERROR invalid unicode character escape
}


