tests/ui/consts/const-eval/promoted_raw_ptr_ops.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &'static bool = &(42 as *const i32 == 43 as *const i32);
    //~^ ERROR temporary value dropped while borrowed
    let y: &'static usize = &(&1 as *const i32 as usize + 1);
    //~^ ERROR temporary value dropped while borrowed
    let z: &'static i32 = &(unsafe { *(42 as *const i32) });
    //~^ ERROR temporary value dropped while borrowed
    let a: &'static bool = &(main as fn() == main as fn());
    //~^ ERROR temporary value dropped while borrowed
}


