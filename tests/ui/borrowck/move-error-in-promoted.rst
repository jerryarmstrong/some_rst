tests/ui/borrowck/move-error-in-promoted.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #70934

fn f() {
    const C: [S2; 1] = [S2];
    let _ = S1(C[0]).clone();
    //~^ ERROR cannot move out of type `[S2; 1]`
}

#[derive(Clone)]
struct S1(S2);

#[derive(Clone)]
struct S2;

fn main() {
    f();
}


