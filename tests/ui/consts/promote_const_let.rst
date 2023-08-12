tests/ui/consts/promote_const_let.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &'static u32 = {
        let y = 42;
        &y //~ ERROR does not live long enough
    };
    let x: &'static u32 = &{ //~ ERROR temporary value dropped while borrowed
        let y = 42;
        y
    };
}


