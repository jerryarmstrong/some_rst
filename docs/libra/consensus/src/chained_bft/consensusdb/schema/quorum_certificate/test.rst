consensus/src/chained_bft/consensusdb/schema/quorum_certificate/test.rs
=======================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use solana_libra_schemadb::schema::assert_encode_decode;

#[test]
fn test_encode_decode() {
    let qc = QuorumCert::certificate_for_genesis();
    assert_encode_decode::<QCSchema>(&qc.certified_block_id(), &qc);
}


