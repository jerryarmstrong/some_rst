src/tools/miri/tests/fail/stacked_borrows/illegal_write6.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = &mut 0u32;
    let p = x as *mut u32;
    foo(x, p);
}

fn foo(a: &mut u32, y: *mut u32) -> u32 {
    *a = 1;
    let _b = &*a;
    unsafe { *y = 2 }; //~ ERROR: /not granting access .* because that would remove .* which is strongly protected/
    return *a;
}


