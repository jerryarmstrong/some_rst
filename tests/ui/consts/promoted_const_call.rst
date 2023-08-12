tests/ui/consts/promoted_const_call.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_mut_refs)]
#![feature(const_trait_impl)]
struct Panic;
impl const Drop for Panic { fn drop(&mut self) { panic!(); } }
pub const fn id<T>(x: T) -> T { x }
pub const C: () = {
    let _: &'static _ = &id(&Panic);
    //~^ ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed
};

fn main() {
    let _: &'static _ = &id(&Panic);
    //~^ ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed
    let _: &'static _ = &&(Panic, 0).1;
    //~^ ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed
}


