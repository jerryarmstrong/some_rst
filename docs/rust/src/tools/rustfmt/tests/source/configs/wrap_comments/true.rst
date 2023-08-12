src/tools/rustfmt/tests/source/configs/wrap_comments/true.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: true
// rustfmt-max_width: 50
// Wrap comments

fn main() {
    // Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
}

fn code_block() {
    // ```rust
    // let x = 3;
    //
    // println!("x = {}", x);
    // ```
}


