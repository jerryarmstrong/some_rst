tests/ui/thread-local/name-collision.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[allow(non_camel_case_types)]
struct u8;

std::thread_local! {
    pub static A: i32 = f();
    pub static B: i32 = const { 0 };
}

fn f() -> i32 {
    0
}

fn main() {}


