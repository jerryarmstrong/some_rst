datatest-stable/src/macros.rs
=============================

Last edited: 2022-02-01 05:13:53

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// SPDX-License-Identifier: MIT OR Apache-2.0

/// `datatest-stable` test harness entry point. Should be declared in the test module.
///
/// Also, `harness` should be set to `false` for that test module in `Cargo.toml` (see [Configuring
/// a target](https://doc.rust-lang.org/cargo/reference/manifest.html#configuring-a-target)).
#[macro_export]
macro_rules! harness {
    ( $( $name:path, $root:expr, $pattern:expr ),+ $(,)* ) => {
        fn main() {
            let mut requirements = Vec::new();

            $(
                requirements.push(
                    $crate::Requirements::new(
                        $name,
                        stringify!($name).to_string(),
                        $root.to_string(),
                        $pattern.to_string()
                    )
                );
            )+

            $crate::runner(&requirements);
        }
    };
}


