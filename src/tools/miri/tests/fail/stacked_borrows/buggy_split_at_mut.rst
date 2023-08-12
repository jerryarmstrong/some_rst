src/tools/miri/tests/fail/stacked_borrows/buggy_split_at_mut.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod safe {
    use std::slice::from_raw_parts_mut;

    pub fn split_at_mut<T>(self_: &mut [T], mid: usize) -> (&mut [T], &mut [T]) {
        let len = self_.len();
        let ptr = self_.as_mut_ptr();

        unsafe {
            assert!(mid <= len);

            (
                from_raw_parts_mut(ptr, len - mid), // BUG: should be "mid" instead of "len - mid"
                from_raw_parts_mut(ptr.offset(mid as isize), len - mid),
            )
        }
    }
}

fn main() {
    let mut array = [1, 2, 3, 4];
    let (a, b) = safe::split_at_mut(&mut array, 0);
    //~^ ERROR: /retag .* tag does not exist in the borrow stack/
    a[1] = 5;
    b[1] = 6;
}


