tests/ui/cast/casts-issue-46365.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Lorem {
    ipsum: Ipsum //~ ERROR cannot find type `Ipsum`
}

fn main() {
    // Testing `as` casts, so deliberately not using `ptr::null`.
    let _foo: *mut Lorem = 0 as *mut _; // no error here
}


