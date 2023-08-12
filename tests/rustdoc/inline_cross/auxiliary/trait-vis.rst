tests/rustdoc/inline_cross/auxiliary/trait-vis.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "inner"]

pub struct SomeStruct;

fn asdf() {
    const _FOO: () = {
        impl Clone for SomeStruct {
            fn clone(&self) -> Self {
                SomeStruct
            }
        }
    };
}


