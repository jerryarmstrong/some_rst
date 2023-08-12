bpf-rust-programs/prediction-poll/wasm_bindings/src/clock.rs
============================================================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: rs

    use core::convert::TryFrom;
use prediction_poll_data::ClockData;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Clock {
    pub slot: u32, // u64, https://caniuse.com/#feat=bigint
}

#[wasm_bindgen]
impl Clock {
    #[wasm_bindgen(js_name = fromData)]
    pub fn from_data(val: &[u8]) -> Self {
        console_error_panic_hook::set_once();
        Clock {
            slot: u32::try_from(ClockData::from_bytes(val).slot).unwrap(),
        }
    }
}


