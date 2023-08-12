src/tools/rustfmt/tests/target/issue_4936.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[discard_params_doc]
trait Trait {
    fn foo(
        &self,
        /// some docs
        bar: String,
        /// another docs
        baz: i32,
    );
}


