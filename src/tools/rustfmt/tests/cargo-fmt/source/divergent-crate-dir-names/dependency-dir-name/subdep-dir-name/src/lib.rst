src/tools/rustfmt/tests/cargo-fmt/source/divergent-crate-dir-names/dependency-dir-name/subdep-dir-name/src/lib.rs
=================================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(test)]
mod tests {
#[test]
fn sub_test_that_works() {
    assert_eq!(3 + 3, 6);
}
 }


