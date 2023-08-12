src/tools/clippy/tests/ui/module_inception.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::module_inception)]

mod foo {
    mod bar {
        mod bar {
            mod foo {}
        }
        mod foo {}
    }
    mod foo {
        mod bar {}
    }
}

// No warning. See <https://github.com/rust-lang/rust-clippy/issues/1220>.
mod bar {
    #[allow(clippy::module_inception)]
    mod bar {}
}

fn main() {}


