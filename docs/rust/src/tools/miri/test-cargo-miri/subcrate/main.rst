src/tools/miri/test-cargo-miri/subcrate/main.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::env;
use std::path::PathBuf;

fn main() {
    println!("subcrate running");

    fn host_to_target_path(path: String) -> PathBuf {
        use std::ffi::{CStr, CString};

        let path = CString::new(path).unwrap();
        let mut out = Vec::with_capacity(1024);

        unsafe {
            extern "Rust" {
                fn miri_host_to_target_path(
                    path: *const i8,
                    out: *mut i8,
                    out_size: usize,
                ) -> usize;
            }
            let ret = miri_host_to_target_path(path.as_ptr(), out.as_mut_ptr(), out.capacity());
            assert_eq!(ret, 0);
            let out = CStr::from_ptr(out.as_ptr()).to_str().unwrap();
            PathBuf::from(out)
        }
    }

    // CWD should be workspace root, i.e., one level up from crate root.
    let env_dir = env::current_dir().unwrap();
    let crate_dir = host_to_target_path(env::var("CARGO_MANIFEST_DIR").unwrap());
    let crate_dir = crate_dir.parent().unwrap();
    assert_eq!(env_dir, crate_dir);
}


