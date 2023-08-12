tests/run-make-fulldeps/link-cfg/no-deps.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(link_cfg)]

#[link(name = "return1", cfg(foo))]
#[link(name = "return2", cfg(bar))]
extern "C" {
    fn my_function() -> i32;
}

fn main() {
    unsafe {
        let v = my_function();
        if cfg!(foo) {
            assert_eq!(v, 1);
        } else if cfg!(bar) {
            assert_eq!(v, 2);
        } else {
            panic!("unknown");
        }
    }
}


