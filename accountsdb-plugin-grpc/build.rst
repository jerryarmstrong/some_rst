accountsdb-plugin-grpc/build.rs
===============================

Last edited: 2021-11-30 16:15:41

Contents:

.. code-block:: rs

    fn main() {
    tonic_build::compile_protos("../proto/accountsdb.proto")
        .unwrap_or_else(|e| panic!("Failed to compile protos {:?}", e));
}


