tests/ui/parser/macro/macro-incomplete-parse.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! ignored_item {
    () => {
        fn foo() {}
        fn bar() {}
        , //~ ERROR macro expansion ignores token `,`
    }
}

macro_rules! ignored_expr {
    () => ( 1,  //~ ERROR expected one of `.`, `;`, `?`, `}`, or an operator, found `,`

            2 )
}

macro_rules! ignored_pat {
    () => ( 1, 2 ) //~ ERROR macro expansion ignores token `,`
}

ignored_item!();

fn main() {
    ignored_expr!();
    match 1 {
        ignored_pat!() => (),
        _ => (),
    }
}


