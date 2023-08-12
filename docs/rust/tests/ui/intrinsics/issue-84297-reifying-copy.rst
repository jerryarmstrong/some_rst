tests/ui/intrinsics/issue-84297-reifying-copy.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    let _unused = if true {
        core::ptr::copy::<i32>
    } else {
        core::ptr::copy_nonoverlapping::<i32>
    };
}


