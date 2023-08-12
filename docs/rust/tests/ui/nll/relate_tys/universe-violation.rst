tests/ui/nll/relate_tys/universe-violation.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the NLL `relate_tys` code correctly deduces that a
// function returning either argument CANNOT be upcast to one
// that returns always its first argument.
//
// compile-flags:-Zno-leak-check

fn make_it() -> fn(&'static u32) -> &'static u32 {
    panic!()
}

fn main() {
    let a: fn(_) -> _ = make_it();
    let b: fn(&u32) -> &u32 = a; //~ ERROR mismatched types [E0308]
    drop(a);
}


