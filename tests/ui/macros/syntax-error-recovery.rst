tests/ui/macros/syntax-error-recovery.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! values {
    ($($token:ident($value:literal) $(as $inner:ty)? => $attr:meta,)*) => {
        #[derive(Debug)]
        pub enum TokenKind {
            $(
                #[$attr]
                $token $($inner)? = $value,
            )*
        }
    };
}
//~^^^^^ ERROR expected one of `(`, `,`, `=`, `{`, or `}`, found `(String)`
//~| ERROR macro expansion ignores token `(String)` and any following

values!(STRING(1) as (String) => cfg(test),);
//~^ ERROR expected one of `!` or `::`, found `<eof>`

fn main() {}


