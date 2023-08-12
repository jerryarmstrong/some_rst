tests/ui/parser/bad-match.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  let isize x = 5; //~ ERROR expected one of `:`, `;`, `=`, `@`, or `|`, found `x`
  match x;
}


