language/move-stdlib/src/natives/helpers.rs
===========================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use move_vm_runtime::native_functions::NativeFunction;

pub fn make_module_natives(
    natives: impl IntoIterator<Item = (impl Into<String>, NativeFunction)>,
) -> impl Iterator<Item = (String, NativeFunction)> {
    natives
        .into_iter()
        .map(|(func_name, func)| (func_name.into(), func))
}


