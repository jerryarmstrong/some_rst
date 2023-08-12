tests/ui/macros/rfc-3086-metavar-expr/dollar-dollar-has-correct-behavior.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(macro_metavar_expr)]

macro_rules! nested {
    ( $a:ident ) => {
        macro_rules! $a {
            ( $$( $b:ident ),* ) => {
                $$(
                    macro_rules! $b {
                        ( $$$$( $c:ident ),* ) => {
                            $$$$(
                                fn $c() -> &'static str { stringify!($c) }
                            ),*
                        };
                    }
                )*
            };
        }
    };
}

fn main() {
    nested!(a);
    a!(b);
    b!(c);
    assert_eq!(c(), "c");
}


