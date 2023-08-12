tests/ui/type/type-dependent-def-issue-49241.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = vec![0];
    const l: usize = v.count(); //~ ERROR attempt to use a non-constant value in a constant
    let s: [u32; l] = v.into_iter().collect();
    //~^ constant
}


