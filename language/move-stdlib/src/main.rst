language/move-stdlib/src/main.rs
================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use move_stdlib::utils::time_it;

fn main() {
    // Generate documentation
    {
        time_it("Generating stdlib documentation", || {
            std::fs::remove_dir_all(move_stdlib::move_stdlib_docs_full_path()).unwrap_or(());
            //std::fs::create_dir_all(&move_stdlib::move_stdlib_docs_full_path()).unwrap();
            move_stdlib::build_stdlib_doc(&move_stdlib::move_stdlib_docs_full_path());
        });

        time_it("Generating nursery documentation", || {
            std::fs::remove_dir_all(move_stdlib::move_nursery_docs_full_path()).unwrap_or(());
            move_stdlib::build_nursery_doc(&move_stdlib::move_nursery_docs_full_path());
        });

        time_it("Generating error explanations", || {
            std::fs::remove_file(move_stdlib::move_stdlib_errmap_full_path()).unwrap_or(());
            move_stdlib::build_error_code_map(&move_stdlib::move_stdlib_errmap_full_path());
        });
    }
}


