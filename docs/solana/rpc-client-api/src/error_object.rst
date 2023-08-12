rpc-client-api/src/error_object.rs
==================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #[derive(Deserialize, Debug)]
pub struct RpcErrorObject {
    pub code: i64,
    pub message: String,
}


