tests/ui/consts/const-eval/match-test-ptr-null.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // Make sure match uses the usual pointer comparison code path -- i.e., it should complain
    // that pointer comparison is disallowed, not that parts of a pointer are accessed as raw
    // bytes.
    let _: [u8; 0] = [4; {
        match &1 as *const i32 as usize {
            //~^ ERROR pointers cannot be cast to integers during const eval
            0 => 42,
            n => n,
        }
    }];
}


