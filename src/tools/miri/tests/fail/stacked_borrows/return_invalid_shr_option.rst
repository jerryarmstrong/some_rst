src/tools/miri/tests/fail/stacked_borrows/return_invalid_shr_option.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we cannot return a `&` that got already invalidated, not even in an `Option`.
fn foo(x: &mut (i32, i32)) -> Option<&i32> {
    let xraw = x as *mut (i32, i32);
    let ret = Some(unsafe { &(*xraw).1 });
    unsafe { *xraw = (42, 23) }; // unfreeze
    ret //~ ERROR: /retag .* tag does not exist in the borrow stack/
}

fn main() {
    match foo(&mut (1, 2)) {
        Some(_x) => {}
        None => {}
    }
}


