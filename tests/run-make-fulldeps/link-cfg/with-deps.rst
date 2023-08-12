tests/run-make-fulldeps/link-cfg/with-deps.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate dep;

fn main() {
    unsafe {
        let v = dep::my_function();
        if cfg!(foo) {
            assert_eq!(v, 1);
        } else if cfg!(bar) {
            assert_eq!(v, 2);
        } else {
            panic!("unknown");
        }
    }
}


