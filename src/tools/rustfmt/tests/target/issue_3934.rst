src/tools/rustfmt/tests/target/issue_3934.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod repro {
    pub fn push() -> Result<(), ()> {
        self.api.map_api_result(|api| {
            #[allow(deprecated)]
            match api.apply_extrinsic_before_version_4_with_context()? {}
        })
    }
}


