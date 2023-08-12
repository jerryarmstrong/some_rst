src/tools/clippy/tests/ui/author/matches.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(clippy::let_and_return)]

fn main() {
    #[clippy::author]
    let a = match 42 {
        16 => 5,
        17 => {
            let x = 3;
            x
        },
        _ => 1,
    };
}


