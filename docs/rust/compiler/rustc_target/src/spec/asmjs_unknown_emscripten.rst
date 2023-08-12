compiler/rustc_target/src/spec/asmjs_unknown_emscripten.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::{wasm32_unknown_emscripten, LinkerFlavor, Target};

pub fn target() -> Target {
    let mut target = wasm32_unknown_emscripten::target();
    target.add_post_link_args(LinkerFlavor::EmCc, &["-sWASM=0", "--memory-init-file", "0"]);
    target
}


