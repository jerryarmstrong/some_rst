testsuite/libra-fuzzer/src/fuzz_targets/consensus_proposal.rs
=============================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::FuzzTargetImpl;
use solana_libra_consensus::event_processor_fuzzing::{fuzz_proposal, generate_corpus_proposal};
use solana_libra_proptest_helpers::ValueGenerator;

#[derive(Clone, Debug, Default)]
pub struct ConsensusProposal;

impl FuzzTargetImpl for ConsensusProposal {
    fn name(&self) -> &'static str {
        module_name!()
    }

    fn description(&self) -> &'static str {
        "Consensus proposal messages"
    }

    fn generate(&self, _idx: usize, _gen: &mut ValueGenerator) -> Option<Vec<u8>> {
        Some(generate_corpus_proposal())
    }

    fn fuzz(&self, data: &[u8]) {
        fuzz_proposal(data);
    }
}


