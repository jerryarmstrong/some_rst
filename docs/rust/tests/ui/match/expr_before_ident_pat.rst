tests/ui/match/expr_before_ident_pat.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! funny {
    ($a:expr, $b:ident) => {
        match [1, 2] {
            [$a, $b] => {}
        }
    };
}

fn main() {
    funny!(a, a);
    //~^ ERROR cannot find value `a` in this scope
    //~| ERROR arbitrary expressions aren't allowed in patterns
}


