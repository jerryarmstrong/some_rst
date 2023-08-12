tests/ui/associated-consts/mismatched_impl_ty_2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Trait {
    const ASSOC: fn(&'static u32);
}
impl Trait for () {
    const ASSOC: for<'a> fn(&'a u32) = |_| ();
}

fn main() {
    let _ = <() as Trait>::ASSOC;
}


