tests/ui/async-await/multiple-lifetimes/partial-relation.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// run-pass

async fn lotsa_lifetimes<'a, 'b, 'c>(a: &'a u32, b: &'b u32, c: &'c u32) -> (&'a u32, &'b u32)
    where 'b: 'a
{
    drop((a, c));
    (b, b)
}

fn main() {
    let _ = lotsa_lifetimes(&22, &44, &66);
}


