tests/ui/uninhabited/uninhabited-matches-feature-gated.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::zeroed;
enum Void {}

fn main() {
    let x: Result<u32, &'static Void> = Ok(23);
    let _ = match x {   //~ ERROR non-exhaustive
        Ok(n) => n,
    };

    // This is pretty much instant UB. However, we have no choice -- we need to
    // test matching on a reference to `&Void`; we cannot do anything other than
    // just accept the fact that this is UB if `main` did run, but it doesn't;
    // this test only checks that these are feature-gated.
    let x: &Void = unsafe { zeroed() };
    let _ = match x {}; //~ ERROR non-exhaustive

    let x: (Void,) = unsafe { zeroed() };
    let _ = match x {}; //~ ERROR non-exhaustive

    let x: [Void; 1] = unsafe { zeroed() };
    let _ = match x {}; //~ ERROR non-exhaustive

    let x: &[Void] = unsafe { zeroed() };
    let _ = match x {   //~ ERROR non-exhaustive
        &[] => (),
    };

    let x: Void = unsafe { zeroed() };
    let _ = match x {}; // okay

    let x: Result<u32, Void> = Ok(23);
    let _ = match x {   //~ ERROR non-exhaustive
        Ok(x) => x,
    };

    let x: Result<u32, Void> = Ok(23);
    let Ok(x) = x;
    //~^ ERROR refutable
}


