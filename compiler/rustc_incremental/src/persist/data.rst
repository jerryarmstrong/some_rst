compiler/rustc_incremental/src/persist/data.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! The data that we will serialize and deserialize.

use rustc_macros::{Decodable, Encodable};
use rustc_middle::dep_graph::{WorkProduct, WorkProductId};

#[derive(Debug, Encodable, Decodable)]
pub struct SerializedWorkProduct {
    /// node that produced the work-product
    pub id: WorkProductId,

    /// work-product data itself
    pub work_product: WorkProduct,
}


