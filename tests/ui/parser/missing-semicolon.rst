tests/ui/parser/missing-semicolon.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! m {
    ($($e1:expr),*; $($e2:expr),*) => {
        $( let x = $e1 )*; //~ ERROR expected one of `.`, `;`, `?`, `else`, or
        $( println!("{}", $e2) )*;
    }
}

fn main() { m!(0, 0; 0, 0); }


