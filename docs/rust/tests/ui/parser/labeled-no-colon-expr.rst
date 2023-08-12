tests/ui/parser/labeled-no-colon-expr.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    'l0 while false {} //~ ERROR labeled expression must be followed by `:`
    'l1 for _ in 0..1 {} //~ ERROR labeled expression must be followed by `:`
    'l2 loop {} //~ ERROR labeled expression must be followed by `:`
    'l3 {} //~ ERROR labeled expression must be followed by `:`
    'l4 0; //~ ERROR labeled expression must be followed by `:`
    //~^ ERROR expected `while`, `for`, `loop` or `{`

    macro_rules! m {
        ($b:block) => {
            'l5 $b; //~ ERROR cannot use a `block` macro fragment here
        }
    }
    m!({}); //~ ERROR labeled expression must be followed by `:`
}


