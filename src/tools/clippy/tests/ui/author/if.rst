src/tools/clippy/tests/ui/author/if.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(clippy::all)]

fn main() {
    #[clippy::author]
    let _ = if true {
        1 == 1;
    } else {
        2 == 2;
    };

    let a = true;

    #[clippy::author]
    if let true = a {
    } else {
    };
}


