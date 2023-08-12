src/tools/miri/tests/fail/validity/invalid_bool_uninit.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(invalid_value)]

union MyUninit {
    init: (),
    uninit: [bool; 1],
}

fn main() {
    let _b = unsafe { MyUninit { init: () }.uninit }; //~ ERROR: constructing invalid value
}


