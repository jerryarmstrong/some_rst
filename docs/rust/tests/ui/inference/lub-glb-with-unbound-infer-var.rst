tests/ui/inference/lub-glb-with-unbound-infer-var.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test for a specific corner case: when we compute the LUB of two fn
// types and their parameters have unbound variables. In that case, we
// wind up relating those two variables. This was causing an ICE in an
// in-progress PR.

fn main() {
    let a_f: fn(_) = |_| ();
    let b_f: fn(_) = |_| ();
    let c_f = match 22 {
        0 => a_f,
        _ => b_f,
    };
    c_f(4);
}


