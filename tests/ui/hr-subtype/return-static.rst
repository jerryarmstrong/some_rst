tests/ui/hr-subtype/return-static.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn make<T>() -> T {
    panic!()
}

fn take<T>(x: T) {}

fn main() {
    let x: for<'a> fn(&'a u32) -> _ = make();
    let y: &'static u32 = x(&22);
    take::<for<'b> fn(&'b u32) -> &'b u32>(x);
}


