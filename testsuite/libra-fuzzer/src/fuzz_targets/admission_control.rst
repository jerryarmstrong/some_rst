testsuite/libra-fuzzer/src/fuzz_targets/admission_control.rs
============================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::FuzzTargetImpl;
use solana_libra_admission_control_service::admission_control_service::fuzzing::{
    fuzzer, generate_corpus,
};
use solana_libra_proptest_helpers::ValueGenerator;

#[derive(Clone, Debug, Default)]
pub struct AdmissionControlSubmitTransactionRequest;

impl FuzzTargetImpl for AdmissionControlSubmitTransactionRequest {
    fn name(&self) -> &'static str {
        module_name!()
    }

    fn description(&self) -> &'static str {
        "Admission Control SubmitTransactionRequest"
    }

    fn generate(&self, _idx: usize, gen: &mut ValueGenerator) -> Option<Vec<u8>> {
        Some(generate_corpus(gen))
    }

    fn fuzz(&self, data: &[u8]) {
        fuzzer(data);
    }
}


