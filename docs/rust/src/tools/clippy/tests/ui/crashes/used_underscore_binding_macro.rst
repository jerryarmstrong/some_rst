src/tools/clippy/tests/ui/crashes/used_underscore_binding_macro.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use serde::Deserialize;

/// Tests that we do not lint for unused underscores in a `MacroAttribute`
/// expansion
#[deny(clippy::used_underscore_binding)]
#[derive(Deserialize)]
struct MacroAttributesTest {
    _foo: u32,
}

#[test]
fn macro_attributes_test() {
    let _ = MacroAttributesTest { _foo: 0 };
}

fn main() {}


