tests/ui/parser/new-unicode-escapes-4.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let s = "\u{lol}";
     //~^ ERROR invalid character in unicode escape: `l`
}


