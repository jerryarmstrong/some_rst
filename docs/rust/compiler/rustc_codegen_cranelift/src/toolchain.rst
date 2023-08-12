compiler/rustc_codegen_cranelift/src/toolchain.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Locating various executables part of a C toolchain.

use std::path::PathBuf;

use rustc_codegen_ssa::back::link::linker_and_flavor;
use rustc_session::Session;

/// Tries to infer the path of a binary for the target toolchain from the linker name.
pub(crate) fn get_toolchain_binary(sess: &Session, tool: &str) -> PathBuf {
    let (mut linker, _linker_flavor) = linker_and_flavor(sess);
    let linker_file_name =
        linker.file_name().unwrap().to_str().expect("linker filename should be valid UTF-8");

    if linker_file_name == "ld.lld" {
        if tool != "ld" {
            linker.set_file_name(tool)
        }
    } else {
        let tool_file_name = linker_file_name
            .replace("ld", tool)
            .replace("gcc", tool)
            .replace("clang", tool)
            .replace("cc", tool);

        linker.set_file_name(tool_file_name)
    }

    linker
}


