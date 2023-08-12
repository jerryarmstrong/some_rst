tests/ui/issues/issue-2590.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Parser {
    tokens: Vec<isize> ,
}

trait Parse {
    fn parse(&self) -> Vec<isize> ;
}

impl Parse for Parser {
    fn parse(&self) -> Vec<isize> {
        self.tokens //~ ERROR cannot move out
    }
}

fn main() {}


