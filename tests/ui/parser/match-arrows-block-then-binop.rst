tests/ui/parser/match-arrows-block-then-binop.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = match 0 {
      0 => {
        0
      } + 5 //~ ERROR expected pattern, found `+`
    };
}


