bpf-rust-programs/prediction-poll/program_data/src/clock.rs
===========================================================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: rs

    pub struct ClockData {
    pub slot: u64,
}

impl ClockData {
    pub fn from_bytes(data: &[u8]) -> Self {
        Self {
            slot: u64::from_le_bytes(*array_ref!(data, 0, 8)),
        }
    }
}


