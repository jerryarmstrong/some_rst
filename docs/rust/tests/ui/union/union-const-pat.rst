tests/ui/union/union-const-pat.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    union U {
    a: usize,
    b: usize,
}

const C: U = U { a: 10 };

fn main() {
    match C {
        C => {} //~ ERROR cannot use unions in constant patterns
        _ => {}
    }
}


