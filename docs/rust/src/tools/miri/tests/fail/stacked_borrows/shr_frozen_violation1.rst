src/tools/miri/tests/fail/stacked_borrows/shr_frozen_violation1.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: &mut i32) -> i32 {
    *x = 5;
    unknown_code(&*x);
    *x // must return 5
}

fn main() {
    println!("{}", foo(&mut 0));
}

fn unknown_code(x: &i32) {
    unsafe {
        *(x as *const i32 as *mut i32) = 7; //~ ERROR: /write access .* only grants SharedReadOnly permission/
    }
}


