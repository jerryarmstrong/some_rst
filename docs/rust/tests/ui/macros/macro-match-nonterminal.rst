tests/ui/macros/macro-match-nonterminal.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! test {
    ($a, $b) => {
        //~^ ERROR missing fragment
        //~| ERROR missing fragment
        //~| ERROR missing fragment
        //~| WARN this was previously accepted
        //~| WARN this was previously accepted
        ()
    };
}

fn main() {
    test!()
}


