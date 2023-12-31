tests/run-make/coverage/uses_inline_crate.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_assignments, unused_variables)]

// compile-flags: -C opt-level=3 # validates coverage now works with optimizations

extern crate used_inline_crate;

fn main() {
    used_inline_crate::used_function();
    used_inline_crate::used_inline_function();
    let some_vec = vec![1, 2, 3, 4];
    used_inline_crate::used_only_from_bin_crate_generic_function(&some_vec);
    used_inline_crate::used_only_from_bin_crate_generic_function("used from bin uses_crate.rs");
    used_inline_crate::used_from_bin_crate_and_lib_crate_generic_function(some_vec);
    used_inline_crate::used_with_same_type_from_bin_crate_and_lib_crate_generic_function(
        "interesting?",
    );
}


