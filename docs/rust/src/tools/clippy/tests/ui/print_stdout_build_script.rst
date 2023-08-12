src/tools/clippy/tests/ui/print_stdout_build_script.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-name=build_script_build

#![warn(clippy::print_stdout)]

fn main() {
    // Fix #6041
    //
    // The `print_stdout` lint shouldn't emit in `build.rs`
    // as these methods are used for the build script.
    println!("Hello");
    print!("Hello");
}


