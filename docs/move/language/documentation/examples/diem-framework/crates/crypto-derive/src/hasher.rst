language/documentation/examples/diem-framework/crates/crypto-derive/src/hasher.rs
=================================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

/// Converts a camel-case string to snake-case
pub fn camel_to_snake(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut first = true;
    text.chars().for_each(|c| {
        if !first && c.is_uppercase() {
            out.push('_');
            out.extend(c.to_lowercase());
        } else if first {
            first = false;
            out.extend(c.to_lowercase());
        } else {
            out.push(c);
        }
    });
    out
}


