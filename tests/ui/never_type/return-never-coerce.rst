tests/ui/never_type/return-never-coerce.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that ! coerces to other types.

// run-fail
// error-pattern:aah!
// ignore-emscripten no processes

fn call_another_fn<T, F: FnOnce() -> T>(f: F) -> T {
    f()
}

fn wub() -> ! {
    panic!("aah!");
}

fn main() {
    let x: i32 = call_another_fn(wub);
    let y: u32 = wub();
}


