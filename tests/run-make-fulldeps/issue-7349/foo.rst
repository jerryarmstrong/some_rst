tests/run-make-fulldeps/issue-7349/foo.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn outer<T>() {
    #[allow(dead_code)]
    fn inner() -> u32 {
        8675309
    }
    inner();
}

extern "C" fn outer_foreign<T>() {
    #[allow(dead_code)]
    fn inner() -> u32 {
        11235813
    }
    inner();
}

fn main() {
    outer::<isize>();
    outer::<usize>();
    outer_foreign::<isize>();
    outer_foreign::<usize>();
}


