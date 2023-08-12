tests/run-make-fulldeps/cross-lang-lto-pgo-smoketest/main.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "xyz")]
extern "C" {
    fn c_always_inlined() -> u32;
    fn c_never_inlined() -> u32;
}

fn main() {
    unsafe {
        println!("blub: {}", c_always_inlined() + c_never_inlined());
    }
}


