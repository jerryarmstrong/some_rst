src/tools/miri/tests/fail/stacked_borrows/alias_through_mutation.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This makes a ref that was passed to us via &mut alias with things it should not alias with
fn retarget(x: &mut &u32, target: &mut u32) {
    unsafe {
        *x = &mut *(target as *mut _);
    }
}

fn main() {
    let target = &mut 42;
    let mut target_alias = &42; // initial dummy value
    retarget(&mut target_alias, target);
    // now `target_alias` points to the same thing as `target`
    *target = 13;
    let _val = *target_alias; //~ ERROR: /read access .* tag does not exist in the borrow stack/
}


