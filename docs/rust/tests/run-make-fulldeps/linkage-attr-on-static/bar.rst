tests/run-make-fulldeps/linkage-attr-on-static/bar.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(linkage)]

#[no_mangle]
#[linkage = "external"]
static BAZ: i32 = 21;

#[link(name = "foo", kind = "static")]
extern "C" {
    fn what() -> i32;
}

fn main() {
    unsafe {
        assert_eq!(what(), BAZ);
    }
}


