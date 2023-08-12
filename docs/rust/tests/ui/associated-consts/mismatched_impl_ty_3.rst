tests/ui/associated-consts/mismatched_impl_ty_3.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Trait {
    const ASSOC: for<'a, 'b> fn(&'a u32, &'b u32);
}
impl Trait for () {
    const ASSOC: for<'a> fn(&'a u32, &'a u32) = |_, _| ();
}

fn main() {
    let _ = <() as Trait>::ASSOC;
}


